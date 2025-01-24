from pydantic import BaseModel
from typing import Optional, List

class DocumentoCreateSchema(BaseModel):
    id: int
    nome: str
    descricao: str
    tipo: str
    conteudo: str
    data_criacao: str
    data_atualizacao: str
    template: str
    status: str

    class Config:
        orm_mode = True

class DocumentoGetSchema(BaseModel):
    id: int
    nome: str
    descricao: str
    tipo: str
    conteudo: str
    data_criacao: str
    data_atualizacao: str
    template: str
    status: str

    class Config:
        orm_mode = True

class DocumentoListSchema(BaseModel):
    documentos: List[DocumentoGetSchema]

    class Config:
        orm_mode = True

class DocumentoUpdateSchema(BaseModel):
    id: int
    nome: Optional[str]
    descricao: Optional[str]
    tipo: Optional[str]
    conteudo: Optional[str]
    data_criacao: Optional[str]
    data_atualizacao: Optional[str]
    template: Optional[str]
    status: Optional[str]

    class Config:
        orm_mode = True

class DocumentoDeleteSchema(BaseModel):
    id: int
    
    class Config:
        orm_mode = True
        