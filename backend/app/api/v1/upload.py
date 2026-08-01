from fastapi import APIRouter, File, UploadFile
from typing import Annotated

from app.schemas.upload import UploadResponse
from app.services.upload_service import UploadService

router = APIRouter()

service = UploadService()


@router.post(
    "/upload/images",
    response_model=UploadResponse,
)
async def upload_images(
    files: Annotated[list[UploadFile], File(...)]
):

    pages = await service.upload_images(files)

    return UploadResponse(
        message="Images uploaded successfully.",
        pages=pages,
    )


@router.post(
    "/upload/pdf",
    response_model=UploadResponse,
)
async def upload_pdf(
    file: UploadFile = File(...)
):

    pages = await service.upload_pdf(file)

    return UploadResponse(
        message="PDF uploaded successfully.",
        pages=pages,
    )