import cv2
import imutils
import numpy as np
from app.core.exceptions import DocumentException

class DocumentScanner:

    def __init__(self):
        self.resize_height = 500

    def scan(self, image_path: str):

        image = cv2.imread(image_path)

        if image is None:
            raise DocumentException("Unable to read image.")

        original = image.copy()

        ratio = image.shape[0] / self.resize_height

        resized = imutils.resize(
            image,
            height=self.resize_height,
        )

        return original, resized, ratio