from pydantic import BaseModel


class OCRResponse(BaseModel):
    success: bool = True
    session_id: str
    status: str
    processed_pages: int