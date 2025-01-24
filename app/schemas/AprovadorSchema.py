from typing import List, Optional
from pydantic import BaseModel

class AprovadorGetSchema(BaseModel):
    id: int
    perfil: str
    data_criacao: str
    ordem: str
    
    class Config:
        orm_mode = True
    
class AprovadorCreateSchema(BaseModel):
    id: int
    perfil: str
    data_criacao: str
    ordem: str
    data_criacao: str
    
    class Config:
        orm_mode = True

class AprovadorListSchema(BaseModel):
    aprovadores: List[AprovadorGetSchema]
    
    class Config:
        orm_mode = True

class AprovadorUpdateSchema(BaseModel):
    id: int
    perfil: Optional[str]
    data_criacao: Optional[str]
    ordem: Optional[str]
    data_criacao: Optional[str]
    
    class Config:
        orm_mode = True

class AprovadorDeleteSchema(BaseModel):
    id: int
    
    class Config:
        orm_mode = True
