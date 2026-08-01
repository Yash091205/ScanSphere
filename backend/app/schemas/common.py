from typing import Any, Optional

from pydantic import BaseModel


class SuccessResponse(BaseModel):
    """
    Standard response for successful API requests.
    """

    success: bool = True
    message: str
    data: Optional[Any] = None


class ErrorResponse(BaseModel):
    """
    Standard response for failed API requests.
    """

    success: bool = False
    message: str