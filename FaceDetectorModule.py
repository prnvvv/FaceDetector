import cv2
import mediapipe as mp
import time

class FaceDetector:
    def __init__(self, minConfidence=0.5):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("Could not open webcam.")
            exit()

        self.mpFaceDetection = mp.solutions.face_detection
        self.faceDetection = self.mpFaceDetection.FaceDetection(min_detection_confidence = minConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def detectFaces(self):
        previousTime = 0

        while True:
            success, vidObject = self.cap.read()

            if not success:
                print("Could not read frame from webcam.")
                break

            imgRGB = cv2.cvtColor(vidObject, cv2.COLOR_BGR2RGB)
            results = self.faceDetection.process(imgRGB)

            if results.detections:
                for detection in results.detections:
                    boundingBoxC = detection.location_data.relative_bounding_box
                    h, w, c = vidObject.shape
                    xmin = int(boundingBoxC.xmin * w)
                    ymin = int(boundingBoxC.ymin * h)
                    width = int(boundingBoxC.width * w)
                    height = int(boundingBoxC.height * h)
                    topLeft = (xmin, ymin)
                    bottomRight = (xmin + width, ymin + height)

                    cv2.rectangle(vidObject, topLeft, bottomRight, (255, 0, 255), 2)

                    cv2.putText(vidObject, f'{int(detection.score[0] * 100)}%', 
                                (xmin, ymin - 10), 
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            currentTime = time.time()
            fps = 1 / (currentTime - previousTime)
            previousTime = currentTime

            cv2.putText(vidObject, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Face Detection", vidObject)

            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detector = FaceDetector()
    face_detector.detectFaces()
