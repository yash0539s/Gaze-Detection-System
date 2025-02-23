import os
import cv2
import dlib
import winsound  # Use winsound for playback

# Define the absolute path to your alert sound file.
sound_path = r"C:\Users\HP\OneDrive\Desktop\Aissms\sound\alert_fixed.wav"
if not os.path.exists(sound_path):
    print("Error: Missing 'alert_fixed.wav' in sound folder")
    exit()

print("Sound file path:", sound_path)

# Load dlib's face detector and predictor.
detector = dlib.get_frontal_face_detector()
predictor_path = r"C:\Users\HP\OneDrive\Desktop\Aissms\shape_predictor_68_face_landmarks.dat"
if not os.path.exists(predictor_path):
    print("Error: Missing 'shape_predictor_68_face_landmarks.dat'")
    exit()

predictor = dlib.shape_predictor(predictor_path)

# Initialize the webcam.
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Starting face detection. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Face detected! Playing sound...")
        try:
            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception as e:
            print("Error during sound playback:", e)

    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
