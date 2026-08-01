from app.utils.session_manager import SessionManager
from pathlib import Path
from fastapi import UploadFile
from app.core.config import MAX_FILE_SIZE_MB
from app.core.exceptions import UploadException

class ReviewService:

    def get_session(self, session_id: str):

        manager = SessionManager(session_id)

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