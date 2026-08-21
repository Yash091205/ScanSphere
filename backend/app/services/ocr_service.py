from app.ocr.ocr_engine import (
    extract_ocr_data,
    save_ocr_json,
)
from app.utils.session_manager import SessionManager


class OCRService:

    def process_session(
        self,
        session_id: str,
        page_selections,
    ):

        manager = SessionManager(session_id)

        upload_path = manager.get_session_path()
        enhanced_path = manager.get_enhanced_path()
        ocr_path = manager.get_ocr_path()

        processed_count = 0

        for selection in page_selections:

            page_id = selection.page_id
            source = selection.source

            metadata = manager.read_metadata()
            pages_dict = metadata.get("pages", {})

            page_info = pages_dict.get(page_id)

            if not page_info:
                continue

            stored_name = page_info.get(
                "stored_name",
                f"{page_id}.png"
            )

            # Choose the image according to user's selection
            if source == "enhanced":

                image_path = enhanced_path / stored_name

            elif source == "original":

                image_path = upload_path / stored_name

            else:
                continue

            if not image_path.exists():
                continue

            data = extract_ocr_data(str(image_path))

            output = ocr_path / f"{page_id}.json"

            save_ocr_json(
                output,
                data,
            )

            processed_count += 1

        manager.update_status("ocr_completed")

        return {
            "session_id": session_id,
            "status": "ocr_completed",
            "processed_pages": processed_count,
        }