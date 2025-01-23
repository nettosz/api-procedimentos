from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class PerfilModel(Base):
    __tablename__ = 'perfis'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    descricao = Column(String)

    #One to one com permissoes (Um para um perfil)
    permissao_id = Column(Integer, ForeignKey('permissoes.id'))
    permissoes = relationship("PermissaoModel", back_populates="perfil")

    # One to many com usuario (Um para muitos usuários)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship("UsuarioModel", back_populates="perfil")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)
    
    # One to One com usuário (Um para um usuário)
    usuario_aprovador_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario_aprovador = relationship("UsuarioModel", back_populates="perfil_aprovador")

    def __repr__(self):
        return f'<PerfilModel id={self.id} nome={self.nome} descricao={self.descricao} usuario_id={self.usuario_id} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao}>'
    