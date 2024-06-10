import cv2
import mediapipe
import time

capture = cv2.VideoCapture(0)

if not capture.isOpened:
    print("Webcam Cap is on.")
    exit()

while True:
    success, vidObject = cv2.read()

    if not success:
        print("Video Capture failed.")
        
