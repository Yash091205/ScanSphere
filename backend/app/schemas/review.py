from pydantic import BaseModel


class ReviewPage(BaseModel):
    page_number: int
    stored_name: str
    preview_url: str


class ReviewResponse(BaseModel):
    success: bool = True

    session_id: str

    status: str

    document_type: str

    original_file: str

    total_pages: int

    pages: list[ReviewPage]

class ReorderRequest(BaseModel):
    page_order: list[int]


class OCRPage(BaseModel):
    page: str
    text: str


class OCRReviewResponse(BaseModel):
    session_id: str
    pages: list[OCRPage]


class SaveReviewRequest(BaseModel):
    pages: list[OCRPage]