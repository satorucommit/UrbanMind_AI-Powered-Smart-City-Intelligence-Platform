from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None

class PaginatedResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: List[T]
    total: int
    page: int
    per_page: int
    total_pages: int

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error_code: Optional[str] = None