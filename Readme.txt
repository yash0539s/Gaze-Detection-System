Gaze Detection Alert System

This project uses OpenCV, dlib, and OpenFace to detect a user's gaze via a webcam. It provides visual feedback by marking the user's eye region and playing an alert sound when the user looks away from the screen. This can be useful for monitoring user engagement in applications like online learning or driver attention detection.

Table of Contents

Overview

Features

Requirements

Installation

Folder Structure

Usage

Troubleshooting

License

Overview

This application uses OpenCV and dlib for real-time gaze detection. It detects the eye landmarks and tracks pupil movement to determine if the user is looking away. If gaze deviation is detected beyond a predefined threshold, an alert sound is triggered.

Unlike other gaze tracking methods that rely on external hardware, this system operates with just a standard webcam. The alert sound is played using Windows' built-in winsound module, ensuring smooth performance without temporary file permission issues.

Features

✅ Real-Time Gaze Detection:
Uses dlib's 68 facial landmarks to track eye position and determine where the user is looking.

✅ Visual Feedback:
Draws markers around the eyes and displays gaze direction.

✅ Audio Alert:
Plays an alert sound when the user looks away from the screen for too long.

✅ Simple Setup:
Uses only a webcam and built-in Python libraries to function efficiently.

Requirements

Python 3.6 or later

OpenCV (for video capturing and image processing)

bash
Copy
Edit
pip install opencv-python
dlib (for face and landmark detection)

bash
Copy
Edit
pip install dlib
winsound (built-in on Windows for audio alerts)

A valid WAV file (alert sound must be in WAV format, e.g., signed 16-bit PCM)

Installation

Clone or download the repository to your local machine.

Install the required Python packages using pip:

bash
Copy
Edit
pip install opencv-python dlib
Ensure the following files are present:

gaze_detection.py (the main script)

shape_predictor_68_face_landmarks.dat (Dlib's pre-trained model file, downloadable from dlib.net)

sound/alert_fixed.wav (your alert sound file; ensure it plays correctly in a media player)

Folder Structure

bash
Copy
Edit
Gaze_Detection_Project/
├── gaze_detection.py             # Main Python script
├── shape_predictor_68_face_landmarks.dat  # Dlib pre-trained model file
├── sound/
│   └── alert_fixed.wav           # Alert sound file in WAV format
└── README.md                     # This file
Usage
Open a Command Prompt or PowerShell window as Administrator (this helps avoid permission issues).

Navigate to the project folder:

bash
Copy
Edit
cd <path_to_project>/Gaze_Detection_Project
Run the script:

bash
Copy
Edit
python gaze_detection.py
The webcam window will open.

The program will track your gaze and highlight your eyes.

If you look away for more than 2 seconds, an alert sound will play.

Press q to exit the application.

Troubleshooting
🔊 Sound Not Playing?

Ensure sound/alert_fixed.wav plays correctly in a media player.

Confirm that the WAV file is in the correct signed 16-bit PCM format.

Check system volume and make sure the correct playback device is selected.

Verify the absolute path to the WAV file in the script.

🔒 Permission Errors?

Try running the script as an Administrator.

Ensure your environment does not restrict file execution.

📷 Webcam Not Working?

Ensure the webcam is properly connected and not in use by another application.

Check webcam permissions in Windows Privacy Settings.

License
This project is open source and available under the MIT License.
