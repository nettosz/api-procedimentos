from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class TemplateAprovacaoModel(Base):
    __tablename__ = 'templates_aprovacao'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String) 
    
    aprovacao_id = Column(Integer, ForeignKey('aprovacao.id'))
    aprovacoes = relationship("AprovacaoModel", back_populates="template_aprovacao")

    data_criacao = Column(DateTime, default=datetime.datetime.now())

    aprovador_id = Column(Integer, ForeignKey('aprovador.id'))
    aprovadores = relationship("AprovadorModel", back_populates="template_aprovacao")
    
    def __repr__(self):
        return f'<TemplateAprovacao id={self.id} nome={self.nome} descricao={self.descricao} data_criacao={self.data_criacao}>'
    