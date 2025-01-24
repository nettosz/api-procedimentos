from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.database import Base
from sqlalchemy.orm import relationship
import datetime

class UsuarioModel(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, index=True)
    hash_senha = Column(String)

    perfil_id = Column(Integer, ForeignKey('perfis.id'), nullable=False)
    perfil = relationship("PerfilModel", back_populates="usuarios")
    
    data_criacao = Column(DateTime, default=datetime.datetime.now())
    aprovador_flag = Column(Integer, nullable=False)
    
    perfil_aprovador = relationship("PerfilModel", back_populates="usuario_aprovador")

    def __repr__(self):
        return f'<UsuarioModel id={self.id} nome={self.nome} email={self.email} hash_senha={self.hash_senha} perfil_id={self.perfil_id} data_criacao={self.data_criacao} aprovador_flag={self.aprovador_flag}>'
    