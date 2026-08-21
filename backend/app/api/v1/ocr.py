from fastapi import APIRouter

from app.schemas.ocr import OCRRequest, OCRResponse
from app.services.ocr_service import OCRService

router = APIRouter()

service = OCRService()


@router.post(
    "/session/{session_id}/ocr",
    response_model=OCRResponse,
)
def process_ocr(
    session_id: str,
    request: OCRRequest,
):

    result = service.process_session(
        session_id,
        request.pages,
    )

    return OCRResponse(
        session_id=result["session_id"],
        status=result["status"],
        processed_pages=result["processed_pages"],
    )