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

    imgRGB = cv2.cvtColor(vidObject, cv2.COLOR_BAYER_BG2RGB)
    results = FaceDetection.process(imgRGB)

    detections = results.detections

    if detections:
        for id, detection in enumerate(detections):
            boundingBoxC = detection.location_data.relative_bounding_box
            h, w, c = vidObject.shape
            boundingBox = int(boundingBoxC.xmin * w), int(boundingBoxC.ymin * h)

    if not success:
        print("Video Capture failed.")

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
