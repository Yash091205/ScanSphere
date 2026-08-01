import fitz
from PIL import Image
import io
from pathlib import Path


def pdf_to_images(pdf_path: Path, output_folder: Path):
    document = fitz.open(pdf_path)

    image_paths = []

    for page_index in range(len(document)):
        page = document.load_page(page_index)

        pix = page.get_pixmap(dpi=300)

        image = Image.open(io.BytesIO(pix.tobytes("png")))

        output = output_folder / f"page_{page_index+1}.png"

        image.save(output)

        image_paths.append(output)

    document.close()

    return image_paths