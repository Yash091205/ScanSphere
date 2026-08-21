from pydantic import BaseModel
from typing import List


class UploadedPage(BaseModel):
    id: str
    page_id: str
    original_name: str
    stored_name: str
    page_number: int
    preview_url: str
    enhanced_preview_url: str | None = None


class UploadResponse(BaseModel):
    success: bool = True
    message: str
    session_id: str
    pages: List[UploadedPage]