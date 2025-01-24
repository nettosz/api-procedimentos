from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class DocumentoModel(Base):
    __tablename__ = 'documentos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String) 
    tipo_id = Column(Integer, ForeignKey('tipo.id'), nullable=False)
    tipos = relationship("TipoModel", back_populates="documentos")              

    conteudo_id = Column(Integer, ForeignKey('documento_conteudo.id'))
    conteudos = relationship("DocumentoConteudoModel", back_populates="documento")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)
    
    template_aprovacao_id = Column(Integer, ForeignKey('templates_aprovacao.id'))
    templates_aprovacao = relationship("TemplateAprovacaoModel", back_populates="documento")
    
    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)
    status = relationship("StatusModel", back_populates="documentos")

    notificacao_id = Column(Integer, ForeignKey('notificacoes.id'))
    notificacoes = relationship("NotificacaoModel", back_populates="documento")

    aprovacoes = relationship("AprovacaoModel", back_populates="documento")

    def __repr__(self):
        return f'<DocumentoModel id={self.id} nome={self.nome} descricao={self.descricao} tipo_id={self.tipo_id} conteudo_id={self.conteudo_id} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao} template_aprovacao_id={self.template_aprovacao_id} status_id={self.status_id} notificacao_id={self.notificacao_id}>'