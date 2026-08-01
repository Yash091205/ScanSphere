import cv2
import numpy as np
from pathlib import Path
from app.utils.session_manager import SessionManager

def enhance_image(image_path: str):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read image.")

    # 1. Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Noise Removal
    denoised = cv2.fastNlMeansDenoising(gray)

    # 3. Contrast Enhancement
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8),
    )
    contrast = clahe.apply(denoised)

    # 4. Sharpen
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ])

    sharpen = cv2.filter2D(
        contrast,
        -1,
        kernel,
    )

    # 5. Adaptive Threshold
    enhanced = cv2.adaptiveThreshold(
        sharpen,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        10,
    )

    return enhanced




def enhance_session(session_id: str):

    manager = SessionManager(session_id)

    upload_path = manager.get_session_path()
    enhanced_path = manager.get_enhanced_path()

    pages = manager.list_pages()

    for page in pages:

        image_path = upload_path / page["stored_name"]

        enhanced = enhance_image(str(image_path))

        output_path = enhanced_path / page["stored_name"]

        cv2.imwrite(
            str(output_path),
            enhanced,
        )

    return len(pages)