from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class AprovadorModel(Base):
    __tablename__ = 'aprovador'

    id = Column(Integer, primary_key=True, index=True)
    perfil_id = Column(Integer, ForeignKey('perfis.id'), nullable=False)
    perfil = relationship("PerfilModel", back_populates="aprovador")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)
    ordem = Column(Integer, nullable=False)

    template_id = Column(Integer, ForeignKey('templates_aprovacao.id'), nullable=False)
    template_aprovacao = relationship("TemplateAprovacaoModel", back_populates="aprovadores")

    def __repr__(self):
        return f'<AprovadorModel id={self.id} perfil_id={self.perfil_id} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao} ordem={self.ordem} template_id={self.template_id}>'
    