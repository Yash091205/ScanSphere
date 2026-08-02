import cv2
import numpy as np


def order_points(pts):

    x_sorted = pts[np.argsort(pts[:, 0]), :]

    left = x_sorted[:2]
    right = x_sorted[2:]

    left = left[np.argsort(left[:, 1])]
    (tl, bl) = left

    d = np.linalg.norm(right - tl, axis=1)

    (br, tr) = right[np.argsort(d)[::-1]]

    return np.array(
        [tl, tr, br, bl],
        dtype=np.float32,
    )