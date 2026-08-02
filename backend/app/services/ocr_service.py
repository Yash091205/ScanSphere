from pathlib import Path

from app.ocr.ocr_engine import (
    extract_ocr_data,
    save_ocr_json,
)
from app.utils.session_manager import SessionManager


class OCRService:

    def process_session(
        self,
        session_id: str,
    ):

        manager = SessionManager(session_id)

        enhanced_path = manager.get_enhanced_path()
        ocr_path = manager.get_ocr_path()

        image_extensions = {
            ".png",
            ".jpg",
            ".jpeg",
            ".webp",
        }

        image_files = [
            file
            for file in enhanced_path.iterdir()
            if file.is_file()
            and file.suffix.lower() in image_extensions
        ]

        image_files.sort(
            key=lambda file: int(file.stem.split("_")[1])
        )

        for image in image_files:

            data = extract_ocr_data(str(image))

            output = ocr_path / f"{image.stem}.json"

            save_ocr_json(
                output,
                data,
            )

        manager = SessionManager(session_id)
        manager.update_status("ocr_completed")  

        return {
            "session_id": session_id,
            "status": "ocr_completed",
            "processed_pages": len(image_files),
        }