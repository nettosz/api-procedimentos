from pydantic import BaseModel

class PerfilCreateSchema(BaseModel):
    id: str
    nome: str
    Descricao: str
    Aprovacoes: str
    data_criacao: str
    aprovador: int
    template_aprovacao: int
    