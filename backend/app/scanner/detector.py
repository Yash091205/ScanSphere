from dataclasses import dataclass

import cv2
import numpy as np


@dataclass
class DetectionResult:
    success: bool
    contour: np.ndarray | None
    area: float


def detect_document(edges):

    height, width = edges.shape[:2]

    image_area = height * width

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True,
    )

    margin = 10

    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore tiny contours
        if area < image_area * 0.20:
            continue

        perimeter = cv2.arcLength(
            contour,
            True,
        )

        approx = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            True,
        )

        if len(approx) != 4:
            continue

        x, y, w, h = cv2.boundingRect(approx)

        # Reject contours touching the image border
        if (
            x <= margin
            or y <= margin
            or x + w >= width - margin
            or y + h >= height - margin
        ):
            continue

        return DetectionResult(
            success=True,
            contour=approx.reshape(4, 2),
            area=area,
        )

    return DetectionResult(
        success=False,
        contour=None,
        area=0,
    )