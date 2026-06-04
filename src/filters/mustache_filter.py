import cv2

from utils.overlay import overlay_png


class MustacheFilter:

    def __init__(self):

        self.mustache_png = cv2.imread(
            "../assets/mustache.png",
            cv2.IMREAD_UNCHANGED
        )

    def apply(self, frame, face_landmarks):

        h, w, _ = frame.shape

        nose = face_landmarks.landmark[1]
        lip = face_landmarks.landmark[13]

        nose_x = int(nose.x * w)
        nose_y = int(nose.y * h)

        lip_x = int(lip.x * w)
        lip_y = int(lip.y * h)

        mustache_distance = abs(
            lip_y - nose_y
        )

        mustache_width = int(
            mustache_distance * 3.5
        )

        aspect_ratio = (
            self.mustache_png.shape[0]
            / self.mustache_png.shape[1]
        )

        mustache_height = int(
            mustache_width * aspect_ratio
        )

        resized_mustache = cv2.resize(
            self.mustache_png,
            (mustache_width, mustache_height)
        )

        mustache_x = (
            nose_x - mustache_width // 2
        )

        mustache_center_y = (
            nose_y + lip_y
        ) // 2

        mustache_y = (
            mustache_center_y
            - mustache_height // 2
            
        )

        frame = overlay_png(
            frame,
            resized_mustache,
            mustache_x,
            mustache_y
        )

        return frame