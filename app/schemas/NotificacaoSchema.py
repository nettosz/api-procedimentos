from pydantic import BaseModel

class NotificacaoCreateSchema(BaseModel):
    id:int
    descricao: str 
    documento: int
    conteudo: int
    