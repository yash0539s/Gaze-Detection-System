import cv2
import dlib
import numpy as np
import pygame
import time

# Initialize pygame for alert sound
pygame.mixer.init()
alert_sound = pygame.mixer.Sound("C:\\Users\\HP\\OneDrive\\Desktop\\Aissms\\sound\\alert_fixed.wav")  # Provide your own alert sound file

# Load dlib's face detector and shape predictor model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:\\Users\\HP\\OneDrive\\Desktop\\Aissms\\shape_predictor_68_face_landmarks.dat")  # Update the path

# Start webcam capture
cap = cv2.VideoCapture(0)

LOOK_AWAY_TIME = 2.5  # Time threshold before triggering alert
last_away_time = None
warning_triggered = False

# Define landmark indices for eyes and face orientation
LEFT_EYE = [36, 37, 38, 39, 40, 41]
RIGHT_EYE = [42, 43, 44, 45, 46, 47]
NOSE_TIP = 30
LEFT_CHEEK = 2
RIGHT_CHEEK = 14

def get_eye_aspect_ratio(landmarks, eye_points):
    """
    Calculate Eye Aspect Ratio (EAR) to determine eye openness.
    """
    A = np.linalg.norm(np.array(landmarks[eye_points[1]]) - np.array(landmarks[eye_points[5]]))
    B = np.linalg.norm(np.array(landmarks[eye_points[2]]) - np.array(landmarks[eye_points[4]]))
    C = np.linalg.norm(np.array(landmarks[eye_points[0]]) - np.array(landmarks[eye_points[3]]))
    ear = (A + B) / (2.0 * C)
    return ear

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for dlib
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    warning_message = ""  # Initialize empty message
    ear_avg = 0  # Initialize EAR value
    looking_away = False

    for face in faces:
        # Get facial landmarks
        landmarks = predictor(gray, face)
        landmarks_points = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(68)]

        # Calculate Eye Aspect Ratio (EAR)
        left_ear = get_eye_aspect_ratio(landmarks_points, LEFT_EYE)
        right_ear = get_eye_aspect_ratio(landmarks_points, RIGHT_EYE)

        # Average EAR of both eyes
        ear_avg = (left_ear + right_ear) / 2.0

        # Face orientation detection
        nose_x = landmarks_points[NOSE_TIP][0]
        left_cheek_x = landmarks_points[LEFT_CHEEK][0]
        right_cheek_x = landmarks_points[RIGHT_CHEEK][0]

        if ear_avg < 0.2:
            looking_away = True  # Eyes are closed (could mean looking away)
        elif nose_x < left_cheek_x - 20:  
            looking_away = True  # Looking too much to the left
        elif nose_x > right_cheek_x + 20:  
            looking_away = True  # Looking too much to the right

        if looking_away:
            if last_away_time is None:
                last_away_time = time.time()
            elif time.time() - last_away_time > LOOK_AWAY_TIME:
                warning_message = "⚠️ WARNING: You are looking away!"
                if not warning_triggered:
                    alert_sound.play()
                    warning_triggered = True
        else:
            last_away_time = None
            warning_triggered = False

        # Draw landmarks
        for idx in LEFT_EYE + RIGHT_EYE + [NOSE_TIP, LEFT_CHEEK, RIGHT_CHEEK]:
            cv2.circle(frame, landmarks_points[idx], 2, (0, 255, 0), -1)

    # Show EAR value on screen
    cv2.putText(frame, f"EAR: {ear_avg:.2f}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Show warning message if triggered
    if warning_message:
        cv2.putText(frame, warning_message, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("Real-Time Gaze Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
