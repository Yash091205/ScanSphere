from pydantic import BaseModel


class ReviewPage(BaseModel):
    id: str
    page_id: str
    page_number: int
    stored_name: str
    original_name: str
    preview_url: str
    enhanced_preview_url: str | None = None


class ReviewResponse(BaseModel):
    success: bool = True

    session_id: str

    status: str

    document_type: str

    original_file: str

    total_pages: int

    pages: list[ReviewPage]

class ReorderRequest(BaseModel):
    page_order: list[str]


class OCRPage(BaseModel):
    page: str
    text: str


class OCRReviewResponse(BaseModel):
    session_id: str
    pages: list[OCRPage]


class SaveReviewRequest(BaseModel):
    pages: list[OCRPage]