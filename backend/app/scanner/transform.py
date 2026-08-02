import cv2
import numpy as np

from app.scanner.geometry import order_points


def perspective_transform(image, pts):

    rect = order_points(pts)

    tl, tr, br, bl = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)

    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxHeight = max(int(heightA), int(heightB))

    dst = np.array(
        [
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1],
        ],
        dtype=np.float32,
    )

    M = cv2.getPerspectiveTransform(rect, dst)

    warped = cv2.warpPerspective(
        image,
        M,
        (maxWidth, maxHeight),
    )

    return warped