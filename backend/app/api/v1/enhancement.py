from fastapi import APIRouter

from app.schemas.enhancement import EnhancementResponse
from app.services.enhancement_service import EnhancementService

router = APIRouter()

service = EnhancementService()


@router.post(
    "/session/{session_id}/enhance",
    response_model=EnhancementResponse,
)
def enhance_session(session_id: str):

    result = service.enhance(session_id)

    return EnhancementResponse(
        session_id=result["session_id"],
        status=result["status"],
        document_type=result["document_type"],
        original_file=result["original_file"],
        total_pages=result["total_pages"],
        pages=result["pages"],
    )