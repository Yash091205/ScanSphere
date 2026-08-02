from fastapi import APIRouter

from app.services.document_service import DocumentService

router = APIRouter()

service = DocumentService()


@router.post(
    "/session/{session_id}/document",
)
def generate_document(session_id: str):

    return service.generate_docx(session_id)

@router.get(
    "/session/{session_id}/download",
)
def download_document(session_id: str):

    return service.download_docx(session_id)