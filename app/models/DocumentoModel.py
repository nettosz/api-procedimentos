from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class DocumentoModel(Base):
    __tablename__ = 'documentos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String) 
    
    #Many to one com Tipo (Muitos para um tipo)
    tipo_id = Column(Integer, nullable=False)
    tipos = relationship("TipoModel", back_populates="documentos")              

    #One to many com Conteudo (Um para muitos conteúdos)
    conteudo_id = Column(Integer, ForeignKey('conteudos.id'))
    conteudos = relationship("DocumentoConteudoModel", back_populates="documento")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)
    
    #Many to one com TemplateAprovacao (Muitos para um template de aprovação)
    template_aprovacao_id = Column(Integer, ForeignKey('templates_aprovacao.id'))
    templates_aprovacao = relationship("TemplateAprovacao", back_populates="documento")
    
    # Many to one com status (Muitos para um status)
    status_id = Column(Integer, nullable=False)
    status = relationship("StatusModel", back_populates="documentos")

    # One to many com Notificacao (Um para muitas notificações)
    notificacao_id = Column(Integer, ForeignKey('notificacoes.id'))
    notificoes = relationship("NotificacaoModel", back_populates="documento")

    def __repr__(self):
        return f'<DocumentoModel id={self.id} nome={self.nome} descricao={self.descricao} tipo_id={self.tipo_id} conteudo_id={self.conteudo_id} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao} template_aprovacao_id={self.template_aprovacao_id} status_id={self.status_id} notificacao_id={self.notificacao_id}>'
