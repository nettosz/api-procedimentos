from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class StatusModel(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    data_criacao = Column(DateTime, default=datetime.datetime.now())

    #One to many com documentos (Um para varios documentos)
    documentos = relationship("DocumentoModel", back_populates="status")

    #One to many com (Um para varias aprovaçoes)
    aprovacoes = relationship("AprovacaoModel", back_populates="status")
    
    def __repr__(self):
        return f'<StatusModel id={self.id} nome={self.nome} descricao={self.descricao} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao}>'