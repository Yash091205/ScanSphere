import cv2
import imutils


def preprocess_image(image):

    PROCESS_HEIGHT = 700

    ratio = image.shape[0] / PROCESS_HEIGHT

    resized = imutils.resize(
        image,
        height=PROCESS_HEIGHT,
    )

    gray = cv2.cvtColor(
        resized,
        cv2.COLOR_BGR2GRAY,
    )

    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0,
    )

    edges = cv2.Canny(
        blurred,
        30,
        120,
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (3, 3),
    )

    edges = cv2.dilate(
        edges,
        kernel,
        iterations=1,
    )

    edges = cv2.erode(
        edges,
        kernel,
        iterations=1,
    )

    return {
        "ratio": ratio,
        "resized": resized,
        "gray": gray,
        "edges": edges,
    }