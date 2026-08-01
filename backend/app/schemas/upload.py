from pydantic import BaseModel
from typing import List


class UploadedPage(BaseModel):
    id: str
    original_name: str
    stored_name: str
    page_number: int
    preview_url: str


class UploadResponse(BaseModel):
    success: bool = True
    message: str
    pages: List[UploadedPage]