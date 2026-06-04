import cv2

from utils.overlay import overlay_png


class GlassFilter:

    def __init__(self):

        self.glasses_png = cv2.imread(
            "../assets/glasses.png",
            cv2.IMREAD_UNCHANGED
        )

    def apply(self, frame, face_landmarks):

        h, w, _ = frame.shape

        left_eye = face_landmarks.landmark[33]
        right_eye = face_landmarks.landmark[263]

        left_x = int(left_eye.x * w)
        left_y = int(left_eye.y * h)

        right_x = int(right_eye.x * w)
        right_y = int(right_eye.y * h)

        eye_distance = abs(right_x - left_x)

        glasses_width = int(eye_distance * 1.5)

        aspect_ratio = (
            self.glasses_png.shape[0]
            / self.glasses_png.shape[1]
        )

        glasses_height = int(
            glasses_width * aspect_ratio
        )

        resized_glasses = cv2.resize(
            self.glasses_png,
            (glasses_width, glasses_height)
        )

        center_x = (left_x + right_x) // 2
        center_y = (left_y + right_y) // 2

        glasses_x = center_x - glasses_width // 2
        glasses_y = center_y - glasses_height // 2

        frame = overlay_png(
            frame,
            resized_glasses,
            glasses_x,
            glasses_y
        )

        return frame