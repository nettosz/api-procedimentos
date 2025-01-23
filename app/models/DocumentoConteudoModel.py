from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class DocumentoConteudoModel(Base):
    __tablename__ = 'documento_conteudo'

    id = Column(Integer, index=True, autoincrement=True)
    
    #Conteudo do documento
    conteudo =  Column(String)

    #Versao atual do documento
    versao = Column(String)

    data_criacao = DateTime()