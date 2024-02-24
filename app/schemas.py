from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class CarSchema(BaseModel):
    id: Optional[int] = None
    company: Optional[str] = None
    model: Optional[str] = None

    class Config:
        orm_mode = True

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[CarSchema] = None  # Adjust the type to match your expected result type

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestCar(BaseModel):
    parameter: CarSchema = Field(...)
