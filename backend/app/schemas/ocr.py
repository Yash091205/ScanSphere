from pydantic import BaseModel


class OCRResponse(BaseModel):
    success: bool = True
    session_id: str
    status: str
    processed_pages: int

from pydantic import BaseModel


class OCRPageSelection(BaseModel):
    page_id: str
    source: str


class OCRRequest(BaseModel):
    pages: list[OCRPageSelection]


class OCRResponse(BaseModel):
    success: bool = True
    session_id: str
    status: str
    processed_pages: int