from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.DocumentoModel import Documento
from app.schemas.DocumentoSchema import DocumentoCreateSchema, DocumentoUpdateSchema

def get_documento(db: Session, documento_id: int):
    documento = db.query(Documento).filter(Documento.id == documento_id).first()
    if documento is None:
        raise HTTPException(status_code=404, detail="Documento not found")
    return documento

def get_documentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Documento).offset(skip).limit(limit).all()

def create_documento(db: Session, documento: DocumentoCreateSchema) -> Documento:
    db_documento = Documento(**documento.dict())
    db.add(db_documento)
    db.commit()
    db.refresh(db_documento)
    return db_documento

def update_documento(db: Session, documento_id: int, documento: DocumentoUpdateSchema):
    db_documento = get_documento(db, documento_id)
    for key, value in documento.dict().items():
        setattr(db_documento, key, value)
    db.commit()
    db.refresh(db_documento)
    return db_documento

def delete_documento(db: Session, documento_id: int):
    db_documento = get_documento(db, documento_id)
    db.delete(db_documento)
    db.commit()
    return db_documento

#Criar template -> criar aprovações -> criar documento -> vincular template ao documento