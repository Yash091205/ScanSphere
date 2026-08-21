import json
from pathlib import Path
from uuid import uuid4

from app.core.config import ENHANCED_DIR, UPLOAD_DIR, SCANNED_DIR, OCR_DIR, REVIEW_DIR, OUTPUT_DIR
from app.core.exceptions import UploadException


class SessionManager:

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.session_path = UPLOAD_DIR / session_id
        self.metadata_path = self.session_path / "metadata.json"

    def session_exists(self) -> bool:
        return self.session_path.exists()

    def get_session_path(self) -> Path:
        return self.session_path

    def get_scanned_path(self) -> Path:

        scanned_path = SCANNED_DIR / self.session_id

        scanned_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return scanned_path

    def get_enhanced_path(self) -> Path:

        enhanced_path = ENHANCED_DIR / self.session_id

        enhanced_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return enhanced_path

    def get_ocr_path(self) -> Path:

        ocr_path = OCR_DIR / self.session_id

        ocr_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return ocr_path

    def get_review_path(self) -> Path:

        review_path = REVIEW_DIR / self.session_id

        review_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return review_path

    def get_metadata_path(self) -> Path:
        return self.metadata_path

    def create_metadata(
        self,
        original_file: str,
        document_type: str,
        total_pages: int,
        page_order: list[str] = None,
        pages_dict: dict = None,
    ):

        metadata = {
            "session_id": self.session_id,
            "original_file": original_file,
            "document_type": document_type,
            "total_pages": total_pages,
            "status": "uploaded",
            "page_order": page_order if page_order is not None else [],
            "pages": pages_dict if pages_dict is not None else {},
        }

        with open(self.metadata_path, "w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4)

    def read_metadata(self) -> dict:

        if not self.metadata_path.exists():
            raise UploadException("metadata.json not found.")

        with open(self.metadata_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write_metadata(self, metadata: dict):

        with open(self.metadata_path, "w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4)

    def update_status(
        self,
        status: str,
    ):

        metadata = self.read_metadata()

        metadata["status"] = status

        self.write_metadata(metadata)

    def list_pages(self, source: str = "upload") -> list[dict]:
        """
        List pages in order using session metadata.
        """

        metadata = self.read_metadata()

        if source == "upload":
            preview_prefix = "/temp/uploads"
        elif source == "enhanced":
            preview_prefix = "/temp/enhanced"
        else:
            raise UploadException("Invalid source.")

        page_order = metadata.get("page_order", [])
        pages_dict = metadata.get("pages", {})

        pages = []
        for index, page_id in enumerate(page_order, start=1):
            if page_id in pages_dict:
                page_info = pages_dict[page_id]
                stored_name = page_info.get("stored_name", f"{page_id}.png")
                version = page_info.get("version", 1)
                
                pages.append(
                    {
                        "id": page_id,
                        "page_id": page_id,
                        "page_number": index,
                        "stored_name": stored_name,
                        "original_name": page_info.get("original_name", f"Page {index}"),
                        "preview_url": f"{preview_prefix}/{self.session_id}/{stored_name}?v={version}",
                        "enhanced_preview_url": f"/temp/enhanced/{self.session_id}/{stored_name}?v={version}",
                    }
                )

        return pages

    def delete_page(self, page_id: str):
        """
        Delete a page from the session by page_id.
        """

        metadata = self.read_metadata()
        page_order = metadata.get("page_order", [])
        pages_dict = metadata.get("pages", {})

        if page_id not in page_order:
            raise UploadException(f"Page {page_id} not found.")

        page_info = pages_dict.get(page_id, {})
        stored_name = page_info.get("stored_name", f"{page_id}.png")

        # Remove from page_order and pages_dict
        page_order.remove(page_id)
        pages_dict.pop(page_id, None)

        # Remove physical file if present
        page_path = self.session_path / stored_name
        if page_path.exists():
            page_path.unlink()

        # Also remove enhanced file if present
        enhanced_path = self.get_enhanced_path() / stored_name
        if enhanced_path.exists():
            enhanced_path.unlink()

        metadata["page_order"] = page_order
        metadata["pages"] = pages_dict
        metadata["total_pages"] = len(page_order)

        self.write_metadata(metadata)

    def rename_pages(self):
        """
        Legacy method - no-op in metadata-driven ordering architecture.
        """
        pass

    def update_total_pages(self):
        """
        Update total_pages in metadata.json based on current page_order length.
        """

        metadata = self.read_metadata()
        metadata["total_pages"] = len(metadata.get("page_order", []))
        self.write_metadata(metadata)

    def replace_page(self, page_id: str, contents: bytes, extension: str):

        metadata = self.read_metadata()
        pages_dict = metadata.get("pages", {})

        if page_id not in pages_dict:
            raise UploadException(f"Page {page_id} not found.")

        page_info = pages_dict[page_id]
        old_stored_name = page_info.get("stored_name", f"{page_id}.png")

        # Delete old file
        old_path = self.session_path / old_stored_name
        if old_path.exists():
            old_path.unlink()

        new_stored_name = f"{page_id}{extension}"
        new_path = self.session_path / new_stored_name
        new_path.write_bytes(contents)

        # Update metadata info and increment version for cache control
        page_info["stored_name"] = new_stored_name
        page_info["version"] = page_info.get("version", 1) + 1

        self.write_metadata(metadata)

    def append_pages(self, files: list[tuple[bytes, str, str]]):
        """
        files: list of tuples (file_bytes, extension, original_name)
        """

        metadata = self.read_metadata()
        page_order = metadata.get("page_order", [])
        pages_dict = metadata.get("pages", {})

        for contents, extension, original_name in files:
            page_id = f"p_{uuid4().hex[:8]}"
            stored_name = f"{page_id}{extension}"
            
            new_path = self.session_path / stored_name
            new_path.write_bytes(contents)

            pages_dict[page_id] = {
                "page_id": page_id,
                "stored_name": stored_name,
                "original_name": original_name,
                "version": 1
            }
            page_order.append(page_id)

        metadata["page_order"] = page_order
        metadata["pages"] = pages_dict
        metadata["total_pages"] = len(page_order)

        self.write_metadata(metadata)

    def reorder_pages(self, new_page_order: list[str]):
        """
        Reorder pages according to the given list of page_id strings.
        """

        metadata = self.read_metadata()
        current_order = metadata.get("page_order", [])

        if len(new_page_order) != len(current_order) or set(new_page_order) != set(current_order):
            raise UploadException("Invalid page order.")

        metadata["page_order"] = new_page_order
        self.write_metadata(metadata)

    def get_output_path(self) -> Path:

        output_path = OUTPUT_DIR / self.session_id

        output_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return output_path