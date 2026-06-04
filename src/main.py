import cv2

from detector.face_mesh_detector import FaceMeshDetector

from filters.glass_filter import GlassFilter
from filters.mustache_filter import MustacheFilter
from filters.cat_filter import CatFilter

detector = FaceMeshDetector()

glass_filter = GlassFilter()
mustache_filter = MustacheFilter()
cat_filter = CatFilter()

cap = cv2.VideoCapture(0)

filter_mode = 1

while True:

    success, frame = cap.read()

    if not success:
        break

    results = detector.detect_mesh(frame)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            if filter_mode in [1, 3]:

                frame = glass_filter.apply(
                    frame,
                    face_landmarks
                )

            if filter_mode in [2, 3]:

                frame = mustache_filter.apply(
                    frame,
                    face_landmarks
                )
            if filter_mode == 4:

                frame = cat_filter.apply(
                    frame,
                    face_landmarks
                )

    modes = {
        0: "None",
        1: "Glasses",
        2: "Mustache",
        3: "Both",
        4: "Cat Ears"
    }

    cv2.putText(
        frame,
        f"Filter: {modes[filter_mode]}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "1: Glasses  2: Mustache  3: Both  0: None  4: Cat Ears",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "AR Face Filters",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("1"):
        filter_mode = 1

    elif key == ord("2"):
        filter_mode = 2

    elif key == ord("3"):
        filter_mode = 3

    elif key == ord("0"):
        filter_mode = 0

    elif key == ord("4"):
        filter_mode = 4

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()