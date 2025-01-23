from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class TemplateAprovacao(Base):
    __tablename__ = 'templates_aprovacao'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String) 

    #One to many com aprovações (Um para muitas aprovações)
    aprovacao_id = Column(Integer, ForeignKey('aprovacao.id'))
    aprovacoes = relationship("AprovacaoModel", back_populates="template_aprovacao")

    data_criacao = Column(DateTime, default=datetime.datetime.now())

    # One to many com aprovador (Um para muitos aprovadores)
    aprovador_id = Column(Integer, ForeignKey('aprovador.id'))
    aprovadores = relationship("AprovadorModel", back_populates="template_aprovacao")
    
    # Método mágico para representar a classe como uma string
    def __repr__(self):
        return f'<TemplateAprovacao id={self.id} nome={self.nome} descricao={self.descricao} tipo_id={self.tipo_id} conteudo_id={self.conteudo_id} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao} template_aprovacao_id={self.template_aprovacao_id} status_id={self.status_id} notificacao_id={self.notificacao_id}>'