import cv2

from utils.overlay import overlay_png


class CatFilter:

    def __init__(self):

        self.cat_png = cv2.imread(
            "../assets/cat_ears.png",
            cv2.IMREAD_UNCHANGED
        )

    def apply(self, frame, face_landmarks):

        h, w, _ = frame.shape

        left_eye = face_landmarks.landmark[33]
        right_eye = face_landmarks.landmark[263]

        forehead = face_landmarks.landmark[10]

        left_x = int(left_eye.x * w)
        right_x = int(right_eye.x * w)

        forehead_x = int(forehead.x * w)
        forehead_y = int(forehead.y * h)

        face_width = abs(right_x - left_x)

        ears_width = int(face_width * 2.2)

        aspect_ratio = (
            self.cat_png.shape[0]
            / self.cat_png.shape[1]
        )

        ears_height = int(
            ears_width * aspect_ratio
        )

        resized_ears = cv2.resize(
            self.cat_png,
            (ears_width, ears_height)
        )

        ears_x = (
            forehead_x
            - ears_width // 2
        )

        ears_y = max(
            0,
            forehead_y - ears_height + 50
        )
        
        frame = overlay_png(
            frame,
            resized_ears,
            ears_x,
            ears_y
        )

        return frame