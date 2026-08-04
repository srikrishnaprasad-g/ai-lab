from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    status: str = "success"
    data: Optional[T] = None

class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
