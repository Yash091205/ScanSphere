from fastapi import FastAPI
from app.api.v1.upload import router as upload_router
from app.api.v1.health import router as health_router
from app.api.v1.review import router as review_router
from app.api.v1.document import router as document_router
from app.api.v1.ocr import router as ocr_router
from app.api.v1.enhancement import router as enhancement_router
from app.core.config import PROJECT_NAME, VERSION

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    upload_router,
    prefix="/api/v1",
    tags=["Upload"],
)

app.include_router(
    review_router,
    prefix="/api/v1",
    tags=["Review"],
)

app.include_router(
    enhancement_router,
    prefix="/api/v1",
    tags=["Enhancement"],
)

app.include_router(
    ocr_router,
    prefix="/api/v1",
    tags=["OCR"],
)

app.include_router(
    document_router,
    prefix="/api/v1",
    tags=["Document"],
)