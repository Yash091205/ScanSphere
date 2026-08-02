import cv2

from app.scanner.preprocess import preprocess_image
from app.scanner.detector import detect_document

image_path = input("Image Path: ")

image = cv2.imread(image_path)

result = preprocess_image(image)

detection = detect_document(result["edges"])

output = result["resized"].copy()

if detection.success:

    cv2.polylines(
        output,
        [detection.contour.astype(int)],
        True,
        (0, 255, 0),
        3,
    )

    print("Document Detected")
    print("Area:", detection.area)
    print("Contour:", detection.contour)

else:

    print("Document Not Found")

cv2.imshow("Detection", output)

cv2.waitKey(0)

cv2.destroyAllWindows()