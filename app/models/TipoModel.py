from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.orm import relationship
import datetime

class TipoModel(Base):
    __tablename__ = 'tipo'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    data_criacao = Column(DateTime, default=datetime.datetime.now())    

    documentos = relationship("DocumentoModel", back_populates="tipos")

    def __repr__(self):
        return f'<TipoModel id={self.id} nome={self.nome} descricao={self.descricao} data_criacao={self.data_criacao}>'
    