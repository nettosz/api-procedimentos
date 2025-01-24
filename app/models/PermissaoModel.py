from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class PermissaoModel(Base):
    __tablename__ = 'permissao'
    
    id = Column(Integer, primary_key=True, index=True)
    
    descricao = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)

    perfil_id = Column(Integer, nullable=False)
    perfil = relationship("PerfilModel", back_populates="permissoes")

    def __repr__(self):
        return f'<PermissaoModel id={self.id} descricao={self.descricao} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao}>'
    