from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class DocumentoModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String) 
    
    #Many to one com Tipo (Muitos para um tipo)
    tipo_id = Column(Integer, nullable=False)

    #One to many com Conteudo (Um para muitos conteúdos)
    conteudos = relationship("DocumentoConteudoModel", back_populates="documento")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)
    
    #Many to one com TemplateAprovacao (Muitos para um template de aprovação)
    template_aprovacao_id = Column(Integer, nullable=False)

    # Many to one com status (Muitos para um status)
    status_id = Column(Integer, nullable=False)

    # One to many com Notificacao (Um para muitas notificações)
    notificacoes = relationship("NotificacaoModel", back_populates="documento")
