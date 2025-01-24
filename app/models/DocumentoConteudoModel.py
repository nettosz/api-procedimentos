from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class DocumentoConteudoModel(Base):
    __tablename__ = 'documento_conteudo'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    conteudo = Column(String)
    versao = Column(String)
    data_criacao = Column(DateTime, default=datetime.datetime.now())

    documento_id = Column(Integer, ForeignKey('documentos.id'))
    documento = relationship("DocumentoModel", back_populates="conteudos")

    notificacao = relationship("NotificacaoModel", back_populates="conteudo")

    def __repr__(self):
        return f'<DocumentoConteudoModel id={self.id} conteudo={self.conteudo} versao={self.versao} data_criacao={self.data_criacao}>'
    