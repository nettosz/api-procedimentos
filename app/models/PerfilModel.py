from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class PerfilModel(Base):
    __tablename__ = 'perfis'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)

    permissao_id = Column(Integer, ForeignKey('permissao.id'))
    permissoes = relationship("PermissaoModel", back_populates="perfil")

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship("UsuarioModel", back_populates="perfil")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)
    
    usuario_aprovador_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario_aprovador = relationship("UsuarioModel", back_populates="perfil_aprovador")

    aprovacoes = relationship("AprovacaoModel", back_populates="perfis")
    aprovador = relationship("AprovadorModel", back_populates="perfil")

    def __repr__(self):
        return f'<PerfilModel id={self.id} nome={self.nome} descricao={self.descricao} usuario_id={self.usuario_id} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao}>'
    