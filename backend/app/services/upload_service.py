from uuid import uuid4
from pathlib import Path
from app.utils.session import generate_session_id
from fastapi import UploadFile

from app.core.config import (
    UPLOAD_DIR,
    MAX_FILE_SIZE_MB,
    MAX_PAGE_LIMIT,
)

from app.core.exceptions import UploadException

from app.utils.file_manager import ensure_directory
from app.schemas.upload import UploadedPage
from app.pdf.pdf_converter import pdf_to_images
from app.utils.session_manager import SessionManager

class UploadService:

    def __init__(self):
        ensure_directory(UPLOAD_DIR)

    async def upload_images(self, files: list[UploadFile]):

        if len(files) > MAX_PAGE_LIMIT:
            raise UploadException(
                f"Maximum {MAX_PAGE_LIMIT} pages allowed."
            )

        session_id = generate_session_id()

        manager = SessionManager(session_id)

        session_folder = manager.get_session_path()

        ensure_directory(session_folder)

        uploaded_pages = []
        page_order = []
        pages_dict = {}

        for index, file in enumerate(files, start=1):

            extension = Path(file.filename).suffix.lower()

            if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
                raise UploadException(
                    f"{file.filename} is not a supported image."
                )

            contents = await file.read()

            if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
                raise UploadException(
                    f"{file.filename} exceeds {MAX_FILE_SIZE_MB} MB."
                )

            page_id = f"p_{uuid4().hex[:8]}"
            stored_name = f"{page_id}{extension}"

            destination = session_folder / stored_name

            destination.write_bytes(contents)

            uploaded_pages.append(
                UploadedPage(
                    id=page_id,
                    page_id=page_id,
                    original_name=file.filename,
                    stored_name=stored_name,
                    page_number=index,
                    preview_url=f"/temp/uploads/{session_id}/{stored_name}?v=1",
                )
            )

            page_order.append(page_id)
            pages_dict[page_id] = {
                "page_id": page_id,
                "stored_name": stored_name,
                "original_name": file.filename,
                "version": 1
            }

        manager.create_metadata(
            original_file=files[0].filename if len(files) == 1 else "Multiple Images",
            document_type="images",
            total_pages=len(uploaded_pages),
            page_order=page_order,
            pages_dict=pages_dict,
        )
        
        return {
            "session_id": session_id,
            "pages": uploaded_pages,
        }

    async def upload_pdf(self, pdf: UploadFile):

        if not pdf.filename.lower().endswith(".pdf"):
            raise UploadException("Only PDF files are allowed.")

        contents = await pdf.read()

        if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise UploadException(
                f"PDF exceeds {MAX_FILE_SIZE_MB} MB."
            )

        session_id = generate_session_id()

        session_folder = UPLOAD_DIR / session_id

        ensure_directory(session_folder)

        pdf_path = session_folder / "original.pdf"

        pdf_path.write_bytes(contents)

        page_items = pdf_to_images(pdf_path, session_folder)

        if len(page_items) > MAX_PAGE_LIMIT:
            pdf_path.unlink(missing_ok=True)
            raise UploadException(
                f"PDF contains more than {MAX_PAGE_LIMIT} pages."
            )

        uploaded_pages = []
        page_order = []
        pages_dict = {}

        for index, (page_id, page_file_path) in enumerate(page_items, start=1):
            stored_name = page_file_path.name
            original_name = f"{pdf.filename} (Page {index})"

            uploaded_pages.append(
                UploadedPage(
                    id=page_id,
                    page_id=page_id,
                    original_name=original_name,
                    stored_name=stored_name,
                    page_number=index,
                    preview_url=f"/temp/uploads/{session_id}/{stored_name}?v=1",
                )
            )

            page_order.append(page_id)
            pages_dict[page_id] = {
                "page_id": page_id,
                "stored_name": stored_name,
                "original_name": original_name,
                "version": 1
            }

        pdf_path.unlink(missing_ok=True)

        manager = SessionManager(session_id)

        manager.create_metadata(
            original_file=pdf.filename,
            document_type="pdf",
            total_pages=len(uploaded_pages),
            page_order=page_order,
            pages_dict=pages_dict,
        )

        manager.update_status("uploaded")

        return {
            "session_id": session_id,
            "pages": uploaded_pages,
        }