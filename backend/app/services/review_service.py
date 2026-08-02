from app.utils.session_manager import SessionManager
from pathlib import Path
from fastapi import UploadFile
import json
from app.core.config import MAX_FILE_SIZE_MB
from app.core.exceptions import UploadException

class ReviewService:

    def get_session(self, session_id: str, source: str = "upload"):

        manager = SessionManager(session_id)

        metadata = manager.read_metadata()

        pages = manager.list_pages(source)

        return {
            "session_id": session_id,
            "status": metadata["status"],
            "document_type": metadata["document_type"],
            "original_file": metadata["original_file"],
            "total_pages": metadata["total_pages"],
            "pages": pages,
        }

    def delete_page(self, session_id: str, page_number: int):

        manager = SessionManager(session_id)

        manager.delete_page(page_number)

        manager.rename_pages()

        manager.update_total_pages()

        metadata = manager.read_metadata()

        pages = manager.list_pages()

        return {
            "session_id": session_id,
            "status": metadata["status"],
            "document_type": metadata["document_type"],
            "original_file": metadata["original_file"],
            "total_pages": metadata["total_pages"],
            "pages": pages,
        }

    async def replace_page(
    self,
    session_id: str,
    page_number: int,
    file: UploadFile,
    ):

        extension = Path(file.filename).suffix.lower()

        if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
            raise UploadException("Unsupported image format.")

        contents = await file.read()

        if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise UploadException(
                f"File exceeds {MAX_FILE_SIZE_MB} MB."
            )

        manager = SessionManager(session_id)

        manager.replace_page(page_number, contents, extension)

        metadata = manager.read_metadata()

        pages = manager.list_pages()

        return {
            "session_id": session_id,
            "status": metadata["status"],
            "document_type": metadata["document_type"],
            "original_file": metadata["original_file"],
            "total_pages": metadata["total_pages"],
            "pages": pages,
        }

    async def append_pages(
    self,
    session_id: str,
    files: list[UploadFile],
    ):

        manager = SessionManager(session_id)

        uploaded_files = []

        for file in files:

            extension = Path(file.filename).suffix.lower()

            if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
                raise UploadException("Unsupported image format.")

            contents = await file.read()

            if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
                raise UploadException(
                    f"File exceeds {MAX_FILE_SIZE_MB} MB."
                )

            uploaded_files.append((contents, extension))

        manager.append_pages(uploaded_files)

        metadata = manager.read_metadata()

        pages = manager.list_pages()

        return {
            "session_id": session_id,
            "status": metadata["status"],
            "document_type": metadata["document_type"],
            "original_file": metadata["original_file"],
            "total_pages": metadata["total_pages"],
            "pages": pages,
        }

    def reorder_pages(
        self,
        session_id: str,
        page_order: list[int],
    ):

        manager = SessionManager(session_id)

        manager.reorder_pages(page_order)

        metadata = manager.read_metadata()

        pages = manager.list_pages()

        return {
            "session_id": session_id,
            "status": metadata["status"],
            "document_type": metadata["document_type"],
            "original_file": metadata["original_file"],
            "total_pages": metadata["total_pages"],
            "pages": pages,
        }

    


    def get_ocr_text(self, session_id: str):

        manager = SessionManager(session_id)

        ocr_path = manager.get_ocr_path()

        pages = []

        for file in sorted(ocr_path.glob("*.json")):

            with open(file, encoding="utf-8") as f:
                words = json.load(f)

            text = " ".join(
                word["text"]
                for word in words
            )

            pages.append({
                "page": file.stem,
                "text": text,
            })

        return {
            "session_id": session_id,
            "pages": pages,
        }

    def save_review(
        self,
        session_id: str,
        pages: list,
    ):

        manager = SessionManager(session_id)

        review_path = manager.get_review_path()

        for page in pages:

            file = review_path / f"{page.page}.json"

            with open(file, "w", encoding="utf-8") as f:
                json.dump(
                    page.model_dump(),
                    f,
                    indent=4,
                    ensure_ascii=False,
                )

        return {
            "message": "Review saved successfully."
        }