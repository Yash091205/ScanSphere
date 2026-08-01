from fastapi import FastAPI

from app.api.v1.health import router as health_router
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