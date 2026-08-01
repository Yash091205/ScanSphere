from pydantic import BaseModel


class EnhancementResponse(BaseModel):
    success: bool = True
    session_id: str
    status: str
    enhanced_pages: int