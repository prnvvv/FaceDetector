import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)

if not capture.isOpened:
    print("Webcam Cap is on.")
    exit()

mpFaceDetection = mp.solutions.face_detection
FaceDetection = mpFaceDetection.FaceDetection()
mpDraw = mp.solutions.drawing_utils

currentTime = 0
previousTime = 0

while True:
    success, vidObject = capture.read()

    if not success:
        print("Video Capture failed.")
        break

    imgRGB = cv2.cvtColor(vidObject, cv2.COLOR_BGR2RGB)

    results = FaceDetection.process(imgRGB)

    detections = results.detections

    if detections:
        for id, detection in enumerate(detections):
            boundingBoxC = detection.location_data.relative_bounding_box
            h, w, c = vidObject.shape
            xmin = int(boundingBoxC.xmin * w)
            ymin = int(boundingBoxC.ymin * h)
            width = int(boundingBoxC.width * w)
            height = int(boundingBoxC.height * h)
            topLeft = (xmin, ymin)
            bottomRight = (xmin + width, ymin + height)
            cv2.rectangle(vidObject, topLeft, bottomRight, (255, 0, 255), 2)
            cv2.putText(vidObject, f'fps: {int(detection.score[0] * 100)}%', (xmin, ymin - 10), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 3)

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime

    cv2.imshow("Face Detection", vidObject)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()