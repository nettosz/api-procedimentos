from pydantic import BaseModel
from typing import Optional

class DocumentoCreateSchema(BaseModel):
    title: str
    content: str

class DocumentoUpdateSchema(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

    class Config:
        orm_mode = True