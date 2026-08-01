import json
from pathlib import Path

from app.core.config import ENHANCED_DIR, UPLOAD_DIR
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

    def get_enhanced_path(self) -> Path:

        enhanced_path = ENHANCED_DIR / self.session_id

        enhanced_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return enhanced_path

    def get_metadata_path(self) -> Path:
        return self.metadata_path

    def create_metadata(
        self,
        original_file: str,
        document_type: str,
        total_pages: int,
    ):

        metadata = {
            "session_id": self.session_id,
            "original_file": original_file,
            "document_type": document_type,
            "total_pages": total_pages,
            "status": "uploaded",
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

    def list_pages(self, source: str = "upload") -> list[dict]:
        """
        List pages from upload or enhanced folder.
        """

        if source == "upload":
            folder = self.session_path
            preview_prefix = "/temp/uploads"
        elif source == "enhanced":
            folder = self.get_enhanced_path()
            preview_prefix = "/temp/enhanced"
        else:
            raise UploadException("Invalid source.")

        image_extensions = {".png", ".jpg", ".jpeg", ".webp"}

        pages = []

        image_files = [
            file
            for file in folder.iterdir()
            if file.is_file() and file.suffix.lower() in image_extensions
        ]

        image_files.sort(
            key=lambda file: int(file.stem.split("_")[1])
        )

        for index, file in enumerate(image_files, start=1):

            pages.append(
                {
                    "page_number": index,
                    "stored_name": file.name,
                    "preview_url": f"{preview_prefix}/{self.session_id}/{file.name}",
                }
            )

        return pages

    def delete_page(self, page_number: int):
        """
        Delete a page from the session.
        """

        pages = self.list_pages()

        page = next(
            (
                p
                for p in pages
                if p["page_number"] == page_number
            ),
            None,
        )

        if page is None:
            raise UploadException(
                f"Page {page_number} not found."
            )

        page_path = self.session_path / page["stored_name"]

        page_path.unlink()

    def rename_pages(self):
        """
        Rename pages sequentially after delete or reorder.
        """

        pages = self.list_pages()

        #
        # Step 1
        # Temporary names
        #

        for index, page in enumerate(pages, start=1):

            old_path = self.session_path / page["stored_name"]

            suffix = old_path.suffix

            temp_path = self.session_path / f"temp_{index}{suffix}"

            old_path.rename(temp_path)

        #
        # Step 2
        # Final names
        #

        temp_files = sorted(
            self.session_path.glob("temp_*")
        )

        for index, file in enumerate(temp_files, start=1):

            new_name = f"page_{index}{file.suffix}"

            file.rename(
                self.session_path / new_name
            )

    def update_total_pages(self):
        """
        Update total_pages in metadata.json based on the
        current number of pages in the session.
        """

        metadata = self.read_metadata()

        metadata["total_pages"] = len(self.list_pages())

        self.write_metadata(metadata)

    def replace_page(self, page_number: int, contents: bytes, extension: str):

        pages = self.list_pages()

        page = next(
            (p for p in pages if p["page_number"] == page_number),
            None,
        )

        if page is None:
            raise UploadException(f"Page {page_number} not found.")

        old_path = self.session_path / page["stored_name"]

        old_path.unlink()

        new_path = self.session_path / f"page_{page_number}{extension}"

        new_path.write_bytes(contents)

    def append_pages(self, files: list[tuple[bytes, str]]):

        pages = self.list_pages()

        next_page = len(pages) + 1

        for contents, extension in files:

            new_path = self.session_path / f"page_{next_page}{extension}"

            new_path.write_bytes(contents)

            next_page += 1

        self.update_total_pages()

    def reorder_pages(self, page_order: list[int]):
        """
        Reorder pages according to the given page order.
        Example:
        [3,1,4,2]
        """

        pages = self.list_pages()

        if len(page_order) != len(pages):
            raise UploadException("Invalid page order.")

        #
        # Phase 1 - Rename to temporary names
        #
        for new_index, old_page in enumerate(page_order, start=1):

            page = next(
                p for p in pages
                if p["page_number"] == old_page
            )

            old_path = self.session_path / page["stored_name"]

            suffix = old_path.suffix

            temp_path = self.session_path / f"temp_{new_index}{suffix}"

            old_path.rename(temp_path)

        #
        # Phase 2 - Rename to final names
        #
        temp_files = sorted(
            self.session_path.glob("temp_*")
        )

        for index, file in enumerate(temp_files, start=1):

            new_name = f"page_{index}{file.suffix}"

            file.rename(
                self.session_path / new_name
            )