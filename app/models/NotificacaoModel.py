from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class NotificacaoModel(Base):
    __tablename__ = 'notificacoes'

    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, index=True)
    data_criacao = Column(DateTime, default=datetime.datetime.now())

    documento_id = Column(Integer, ForeignKey('documentos.id'))
    documento = relationship("DocumentoModel", back_populates="notificacoes")

    conteudo_id = Column(Integer, ForeignKey('documento_conteudo.id'))
    conteudo = relationship("DocumentoConteudoModel", back_populates="notificacao")

    def __repr__(self):
        return f'<NotificacaoModel id={self.id} texto={self.texto} data_criacao={self.data_criacao} documento_id={self.documento_id} conteudo_id={self.conteudo_id}>'
    