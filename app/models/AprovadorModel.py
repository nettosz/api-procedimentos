from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime
from sqlalchemy.orm import relationship

class AprovadorModel(Base):
    __tablename__ = 'aprovador'

    id = Column(Integer, primary_key=True, index=True)

    # One to one com perfil (Um para um perfil)
    perfil_id = Column(Integer, nullable=False)
    perfil = relationship("PerfilModel", back_populates="aprovador")

    data_criacao = Column(DateTime, default=datetime.datetime.now())
    data_atualizacao = Column(DateTime)

    #Ordem de aprovação
    ordem = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<AprovadorModel id={self.id} nome={self.nome} email={self.email} senha={self.senha} tipo={self.tipo} data_criacao={self.data_criacao} data_atualizacao={self.data_atualizacao}>'
    