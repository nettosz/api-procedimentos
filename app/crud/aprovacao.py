from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.AprovacaoModel import AprovacaoModel
from app.schemas.AprovacaoSchema import AprovacaoCreateSchema, AprovacaoUpdateSchema

def get_aprovacao(db: Session, aprovacao_id: int):
    aprovacao = db.query(AprovacaoModel).filter(AprovacaoModel.id == aprovacao_id).first()
    if aprovacao is None:
        raise HTTPException(status_code=404, detail="Aprovacao not found")
    return aprovacao

def get_aprovacao_by_documento(db: Session, documento_id: int):
    aprovacao = db.query(AprovacaoModel).filter(AprovacaoModel.documento_id == documento_id).all()
    if aprovacao is None:
        raise HTTPException(status_code=404, detail="Aprovacao not found")
    return aprovacao

def aprovacao_by_status(db: Session, status: int):
    aprovacao = db.query(AprovacaoModel).filter(AprovacaoModel.status == status).all()
    if aprovacao is None:
        raise HTTPException(status_code=404, detail="Aprovacao not found")
    return aprovacao

def get_aprovacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AprovacaoModel).offset(skip).limit(limit).all()

def create_aprovacao(db: Session, aprovacao: AprovacaoCreateSchema) -> AprovacaoModel:
    db_aprovacao = AprovacaoModel(**aprovacao.dict())
    db.add(db_aprovacao)
    db.commit()
    db.refresh(db_aprovacao)
    return db_aprovacao

def update_aprovacao(db: Session, aprovacao_id: int, aprovacao: AprovacaoUpdateSchema):
    db_aprovacao = get_aprovacao(db, aprovacao_id)
    for key, value in aprovacao.dict().items():
        setattr(db_aprovacao, key, value)
    db.commit()
    db.refresh(db_aprovacao)
    return db_aprovacao

def delete_aprovacao(db: Session, aprovacao_id: int):
    db_aprovacao = get_aprovacao(db, aprovacao_id)
    db.delete(db_aprovacao)
    db.commit()
    return db_aprovacao
