# from sqlalchemy import Column, Integer, String, DateTime
# from app.database import Base
# import datetime
# from sqlalchemy.orm import relationship

# #Criação -> Pendente -> Alteracao -> Pendente -> Alteração -> Pendente -> Aprovado -> Publicado
# # Se o aprovador do perfil altualizar para Alteração ele deve selecionar no
# # front-end a area do documento que deve ser alterada, o motivo e o conteudo da alteração
# # O status da aprovação deve ser alteração (para o solicitante da alteração)
# # e o status do documento deve ser alteração
# # O adm de documentos deve aprovar a alteração depois de aplica-la
# # e o status das aprovaçoes deve voltar para pendente

# # Atualizar o status do documento para alteração deve ser bloqueado
# # se houver uma alteração pendente

# class AprovacaoModel(Base):
#     __tablename__ = 'aprovacao'

#     id = Column(Integer, primary_key=True, index=True)
#     # Many to one com perfil (Muitos para um perfil)
#     perfil_id = Column(Integer, nullable=False)
#     perfis = relationship("PerfilModel", back_populates="aprovacoes")

#     # Many to one com documento (Muitos para um documento)
#     documento_id = Column(Integer, nullable=False)
    
#     # (Publicado=4, Criado=3, Aprovado=2, Alteração=1, Pendente=0) // Default Criado ao criar aprovação
#     # Many to one com status (Muitos para um status)
#     status_id = Column(Integer, nullable=False)
#     status = relationship("StatusModel", back_populates="aprovacao")

#     # Data de criação da aprovação
#     data_criacao = Column(DateTime, default=datetime.datetime.now())
    
#     # Data de atualização da aprovação
#     data_atualizacao = Column(DateTime)

#     # Data de expiração da aprovação
#     data_expiracao = Column(DateTime)

#     #ordem de aprovação
#     ordem = Column(Integer, nullable=False)

#     # Método mágico para representar a classe como uma string
#     def __repr__(self):
#         return f'<AprovacaoModel id={self.id} perfil_id={self.perfil_id} procedimento_id={self.procedimento_id} status={self.status} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao} data_expiracao={self.data_expiracao}>'

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class AprovacaoModel(Base):
    __tablename__ = 'aprovacao'

    id = Column(Integer, primary_key=True, index=True)
    perfil_id = Column(Integer, ForeignKey('perfis.id'), nullable=False)
    perfis = relationship("PerfilModel", back_populates="aprovacoes")

    documento_id = Column(Integer, ForeignKey('documentos.id'), nullable=False)
    documento = relationship("DocumentoModel", back_populates="aprovacoes")

    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)
    status = relationship("StatusModel", back_populates="aprovacoes")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)
    data_expiracao = Column(DateTime)
    ordem = Column(Integer, nullable=False)

    template_aprovacao_id = Column(Integer, ForeignKey('templates_aprovacao.id'))
    template_aprovacao = relationship("TemplateAprovacaoModel", back_populates="aprovacoes")

    def __repr__(self):
        return f'<AprovacaoModel id={self.id} perfil_id={self.perfil_id} documento_id={self.documento_id} status={self.status} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao} data_expiracao={self.data_expiracao}>'