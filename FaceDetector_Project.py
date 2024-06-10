import cv2
import mediapipe
import time

capture = cv2.VideoCapture(0)

if not capture.isOpened:
    print("Webcam Cap is on.")
    exit()

currentTime = 0
previousTime = 0

while True:
    success, vidObject = capture.read()

    if not success:
        print("Video Capture failed.")

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
