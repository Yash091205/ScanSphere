import cv2

from app.scanner.preprocess import preprocess_image
from app.scanner.detector import detect_document
from app.scanner.transform import perspective_transform
from app.core.exceptions import DocumentException

class DocumentScanner:

    def scan(self, image_path: str):

        image = cv2.imread(image_path)

        if image is None:
            raise DocumentException(f"Unable to read image: {image_path}")
        processed = preprocess_image(image)

        detection = detect_document(processed["edges"])

        if not detection.success:
            return None

        # Scale contour back to original image size
        contour = detection.contour * processed["ratio"]

        scanned = perspective_transform(
            image,
            contour.astype("float32"),
        )

        return scanned