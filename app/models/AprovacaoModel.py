from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime

#Criação -> Pendente -> Alteracao -> Pendente -> Alteração -> Pendente -> Aprovado -> Publicado
# Se o aprovador do perfil altualizar para Alteração ele deve selecionar no
# front-end a area do documento que deve ser alterada, o motivo e o conteudo da alteração
# O status da aprovação deve ser alteração (para o solicitante da alteração)
# e o status do documento deve ser alteração
# O adm de documentos deve aprovar a alteração depois de aplica-la
# e o status das aprovaçoes deve voltar para pendente

# Atualizar o status do documento para alteração deve ser bloqueado
# se houver uma alteração pendente

class AprovacaoModel(Base):
    __tablename__ = 'aprovacao'

    id = Column(Integer, primary_key=True, index=True)
    # Many to one com perfil (Muitos para um perfil)
    perfil_id = Column(Integer, nullable=False)
    perfis = relationship("PerfilModel", back_populates="aprovacoes")

    # Many to one com documento (Muitos para um documento)
    documento_id = Column(Integer, nullable=False)
    
    # (Publicado=4, Criado=3, Aprovado=2, Alteração=1, Pendente=0) // Default Criado ao criar aprovação
    status = Column(Integer, nullable=False, default=4)
    
    # Data de criação da aprovação
    data_criacao = Column(DateTime, default=datetime.datetime.now())
    
    # Data de atualização da aprovação
    data_atualizacao = Column(DateTime)

    # Data de expiração da aprovação
    data_expiracao = Column(DateTime)

    #ordem de aprovação
    ordem = Column(Integer, nullable=False)

    # Método mágico para representar a classe como uma string
    def __repr__(self):
        return f'<AprovacaoModel id={self.id} perfil_id={self.perfil_id} procedimento_id={self.procedimento_id} status={self.status} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao} data_expiracao={self.data_expiracao}>'
    