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