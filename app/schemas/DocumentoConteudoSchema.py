from typing import List, Optional
from pydantic import BaseModel

class DocumentoConteudoGetSchema(BaseModel):
    id: int
    conteudo:str
    versao:str
    data_criacao: str

    class Config:
        orm_mode = True

class DocumentoConteudoCreateSchema(BaseModel):
    id: int
    conteudo: str
    versao: str
    data_criacao: str

    class Config:
        orm_mode = True

class DocumentoConteudoListSchema(BaseModel):
    aprovadores: List[DocumentoConteudoGetSchema]

    class Config:
        orm_mode = True

class DocumentoConteudoUpdateSchema(BaseModel):
    id: int
    conteudo: Optional[str]
    versao: Optional[str]
    data_criacao: Optional[str]

    class Config:
        orm_mode = True

class DocumentoConteudoDeleteSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True
