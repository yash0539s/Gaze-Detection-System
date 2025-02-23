Face Detection Alert System
This project uses OpenCV and dlib to detect faces via a webcam and plays an alert sound using Windows' built-in winsound module when a face is detected. It is designed to help with applications such as monitoring user engagement or attention.

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
This application leverages the power of OpenCV and dlib to detect faces in a real-time webcam feed. When a face is detected, the system draws a green rectangle around it and plays an alert sound. Instead of using libraries that create temporary files (which can cause permission issues), this project uses the built-in winsound module for audio playback.

Features
Real-Time Face Detection:
Uses dlib's frontal face detector to locate faces in the video stream.

Visual Feedback:
Draws a green rectangle around detected faces.

Audio Alert:
Plays an alert sound (a WAV file) whenever a face is detected.

Simple Setup:
Utilizes Windows' winsound module for audio playback to avoid temporary file permission issues.

Requirements
Python 3.6 or later
OpenCV: For video capturing and image processing
pip install opencv-python
dlib: For face detection and landmark prediction
pip install dlib
winsound: (Built-in on Windows)
A valid WAV file: The alert sound must be in the correct PCM format (WAV (Microsoft) signed 16-bit PCM is recommended).
Installation
Clone or download the repository to your local machine.
Install the required Python packages using pip:
bash
Copy
Edit
pip install opencv-python dlib
Ensure the following files are present:
face_detection.py (the main script)
shape_predictor_68_face_landmarks.dat (Dlib's pre-trained model file; download from dlib.net and extract it)
sound/alert_fixed.wav (your alert sound file; ensure it plays correctly in a media player)
Folder Structure
bash
Copy
Edit
Face_Detection_Project/
├── face_detection.py            # Main Python script
├── shape_predictor_68_face_landmarks.dat  # Dlib pre-trained model file
├── sound/
│   └── alert_fixed.wav          # Alert sound file in WAV format
└── README.md                    # This file
Usage
Open a Command Prompt or PowerShell window as Administrator (this helps avoid potential permission issues).
Navigate to the project folder:
bash
Copy
Edit
cd <path_to_project>/Face_Detection_Project
Run the script:
bash
Copy
Edit
python face_detection.py
The webcam window will open. When a face is detected, a green rectangle will be drawn around it and the alert sound will play asynchronously.
Press q to exit the application.
Troubleshooting
Sound Not Playing:

Double-click sound/alert_fixed.wav to ensure it plays in your default media player.
Confirm that the WAV file is in the proper format (WAV (Microsoft) signed 16-bit PCM is recommended).
Check your system volume and ensure the correct playback device is selected.
Verify that the absolute path to the WAV file is correct (if necessary, modify the path in the script).
Permission Errors:

If you encounter any permission errors, try running the script as an Administrator.
Ensure that your environment does not restrict temporary file creation if using other methods (this version uses winsound to avoid those issues).
Webcam Issues:

Ensure that your webcam is properly connected and not being used by another application.
License
This project is open source and available under the MIT License.