import cv2
import mediapipe as mp


class FaceDetector:

    def __init__(self,
                 model_selection=0,
                 min_detection_confidence=0.5):

        self.mp_face_detection = mp.solutions.face_detection

        self.face_detection = self.mp_face_detection.FaceDetection(
            model_selection=model_selection,
            min_detection_confidence=min_detection_confidence
        )

    def detect_faces(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.face_detection.process(rgb_frame)

        return results