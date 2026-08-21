import fitz
from PIL import Image
import io
from pathlib import Path
from uuid import uuid4


def pdf_to_images(pdf_path: Path, output_folder: Path):
    document = fitz.open(pdf_path)

    page_items = []

    for page_index in range(len(document)):
        page = document.load_page(page_index)

        pix = page.get_pixmap(dpi=300)

        image = Image.open(io.BytesIO(pix.tobytes("png")))

        page_id = f"p_{uuid4().hex[:8]}"
        output = output_folder / f"{page_id}.png"

        image.save(output)

        page_items.append((page_id, output))

    document.close()

    return page_items