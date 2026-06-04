import cv2
import mediapipe as mp


class FaceMeshDetector:

    def __init__(
        self,
        max_num_faces=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ):

        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=max_num_faces,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def detect_mesh(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.face_mesh.process(rgb_frame)

        return results

        