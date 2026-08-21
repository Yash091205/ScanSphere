import json

from pathlib import Path
from docx import Document
from fastapi.responses import FileResponse
from app.core.exceptions import DocumentException
from app.utils.session_manager import SessionManager


class DocumentService:

    def generate_docx(
        self,
        session_id: str,
    ):

        manager = SessionManager(session_id)

        review_path = manager.get_review_path()
        output_path = manager.get_output_path()

        document = Document()

        pages = manager.list_pages()
        review_files_data = []

        for page in pages:
            page_id = page["page_id"]
            review_file = review_path / f"{page_id}.json"
            if review_file.exists():
                with open(review_file, "r", encoding="utf-8") as f:
                    review_files_data.append(json.load(f))

        for index, page in enumerate(review_files_data):

            document.add_paragraph(page["text"])

            if index != len(review_files_data) - 1:
                document.add_page_break()

        output_file = output_path / "output.docx"

        document.save(output_file)
        
        return {
            "session_id": session_id,
            "file_name": output_file.name,
            "message": "Document generated successfully."
        }


    def download_docx(
        self,
        session_id: str,
    ):

        manager = SessionManager(session_id)

        output_path = manager.get_output_path()

        file = output_path / "output.docx"

        if not file.exists():
            raise DocumentException("Document has not been generated yet.")
        return FileResponse(
            path=file,
            filename="output.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )