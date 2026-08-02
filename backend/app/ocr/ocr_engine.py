import pytesseract
from PIL import Image
import json
from pathlib import Path

# If 'tesseract --version' works, you DO NOT need to set tesseract_cmd.
# Leave it commented unless needed.
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_ocr_data(image_path: str):

    image = Image.open(image_path)

    data = pytesseract.image_to_data(
        image,
        lang="eng+hin+mar",
        output_type=pytesseract.Output.DICT,
    )

    results = []

    total = len(data["text"])

    for i in range(total):

        text = data["text"][i].strip()

        if not text:
            continue

        confidence = float(data["conf"][i])

        if confidence < 40:
            continue

        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]

        results.append(
            {
                "text": text,
                "confidence": confidence,
                "bbox": [x, y, w, h],
            }
        )

    return results

def save_ocr_json(
    output_path: Path,
    data: list,
):

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )