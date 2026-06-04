import cv2
import numpy as np


def overlay_png(background, overlay, x, y):

    bg_h, bg_w = background.shape[:2]

    if x >= bg_w or y >= bg_h:
        return background

    h, w = overlay.shape[:2]

    if x + w > bg_w:
        w = bg_w - x
        overlay = overlay[:, :w]

    if y + h > bg_h:
        h = bg_h - y
        overlay = overlay[:h]

    if h <= 0 or w <= 0:
        return background

    if overlay.shape[2] < 4:
        return background

    overlay_img = overlay[:, :, :3]
    alpha_mask = overlay[:, :, 3] / 255.0

    roi = background[y:y+h, x:x+w]

    for c in range(3):

        roi[:, :, c] = (
            alpha_mask * overlay_img[:, :, c]
            + (1 - alpha_mask) * roi[:, :, c]
        )

    background[y:y+h, x:x+w] = roi

    return background