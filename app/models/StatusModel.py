from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class StatusModel(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    data_criacao = Column(DateTime, default=datetime.datetime.now())

    documentos = relationship("DocumentoModel", back_populates="status")
    aprovacoes = relationship("AprovacaoModel", back_populates="status")
    
    def __repr__(self):
        return f'<StatusModel id={self.id} nome={self.nome} data_criacao={self.data_criacao}>'
    