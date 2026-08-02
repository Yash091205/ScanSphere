import cv2

from app.scanner.scanner import DocumentScanner

scanner = DocumentScanner()

image_path = input("Image Path: ")

result = scanner.scan(image_path)

if result is None:
    raise RuntimeError("Document detection failed.")
else:
    cv2.imwrite("scanned_output.jpg", result)
    cv2.imshow("Scanned", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()