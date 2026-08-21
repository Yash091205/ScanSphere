from fastapi import APIRouter
from fastapi import Query
from app.schemas.review import ReorderRequest, OCRReviewResponse, SaveReviewRequest, ReviewResponse
from app.services.review_service import ReviewService
from fastapi import File, UploadFile

router = APIRouter()

service = ReviewService()


@router.get(
    "/session/{session_id}",
    response_model=ReviewResponse,
)
def get_session(session_id: str, source: str = Query("upload")):

    result = service.get_session(session_id, source)

    return ReviewResponse(
        session_id=result["session_id"],
        status=result["status"],
        document_type=result["document_type"],
        original_file=result["original_file"],
        total_pages=result["total_pages"],
        pages=result["pages"],
    )

@router.delete(
    "/session/{session_id}/page/{page_id}",
    response_model=ReviewResponse,
)
def delete_page(
    session_id: str,
    page_id: str,
):

    result = service.delete_page(
        session_id,
        page_id,
    )

    return ReviewResponse(
        session_id=result["session_id"],
        status=result["status"],
        document_type=result["document_type"],
        original_file=result["original_file"],
        total_pages=result["total_pages"],
        pages=result["pages"],
    )

@router.put(
    "/session/{session_id}/page/{page_id}",
    response_model=ReviewResponse,
)
async def replace_page(
    session_id: str,
    page_id: str,
    file: UploadFile = File(...),
):

    result = await service.replace_page(
        session_id,
        page_id,
        file,
    )

    return ReviewResponse(
        session_id=result["session_id"],
        status=result["status"],
        document_type=result["document_type"],
        original_file=result["original_file"],
        total_pages=result["total_pages"],
        pages=result["pages"],
    )

@router.post(
    "/session/{session_id}/append",
    response_model=ReviewResponse,
)
async def append_pages(
    session_id: str,
    files: list[UploadFile] = File(...),
):

    result = await service.append_pages(
        session_id,
        files,
    )

    return ReviewResponse(
        session_id=result["session_id"],
        status=result["status"],
        document_type=result["document_type"],
        original_file=result["original_file"],
        total_pages=result["total_pages"],
        pages=result["pages"],
    )


@router.put(
    "/session/{session_id}/reorder",
    response_model=ReviewResponse,
)
def reorder_pages(
    session_id: str,
    request: ReorderRequest,
):

    result = service.reorder_pages(
        session_id,
        request.page_order,
    )

    return ReviewResponse(
        session_id=result["session_id"],
        status=result["status"],
        document_type=result["document_type"],
        original_file=result["original_file"],
        total_pages=result["total_pages"],
        pages=result["pages"],
    )

@router.get(
    "/session/{session_id}/ocrfetch",
    response_model=OCRReviewResponse,
)
def get_ocr_review(session_id: str):

    result = service.get_ocr_text(session_id)

    return OCRReviewResponse(**result)

@router.put(
    "/session/{session_id}/ocrreview",
)
def save_review(
    session_id: str,
    request: SaveReviewRequest,
):

    return service.save_review(
        session_id,
        request.pages,
    )