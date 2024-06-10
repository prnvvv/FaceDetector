import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)

if not capture.isOpened:
    print("Webcam Cap is on.")
    exit()

mpFaceDetection = mp.solutions.face_detection
FaceDetection = mp.solutions.FaceDetection()
mpDraw = mp.solutions.drawing_utils

currentTime = 0
previousTime = 0

while True:
    success, vidObject = capture.read()

    if not success:
        print("Video Capture failed.")

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
