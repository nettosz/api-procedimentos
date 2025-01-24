from pydantic import BaseModel
from typing import List, Optional

class AprovacaoCreateSchema(BaseModel):
    id: int
    perfil_id: int
    documento_id: int
    status: int
    data_criacao: str
    data_atualizacao: str
    data_expiracao: str
    ordem: int

    class Config:
        orm_mode = True


class AprovacaoGetSchema(BaseModel):
    id: int
    perfil_id: int
    documento_id: int
    status: int
    data_criacao: str
    data_atualizacao: str
    data_expiracao: str
    ordem: int

    class Config:
        orm_mode = True


class AprovacaoListSchema(BaseModel):
    aprovacoes: List[AprovacaoGetSchema]

    class Config:
        orm_mode = True

class AprovacaoUpdateSchema(BaseModel):
    id: int
    perfil_id: Optional[int]
    documento_id: Optional[int]
    status: Optional[int]
    data_criacao: Optional[str]
    data_atualizacao: Optional[str]
    data_expiracao: Optional[str]
    ordem: Optional[int]

    class Config:
        orm_mode = True

class AprovacaoDeleteSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True