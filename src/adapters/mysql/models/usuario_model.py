import uuid
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer
from sqlalchemy.orm import relationship
from src.util.base_declarative import Base

from src.adapters.mysql.models.perfil_model import PerfilModel

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column('id', String(36), primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    dominio_id = Column('dominio_id', String(36), ForeignKey('dominio.id'), primary_key=True, nullable=False)
    nome = Column('nome', String(120), nullable=False)
    email = Column('email', String(70), nullable=False)
    senha = Column('senha', String(72), nullable=False)
    ativo = Column('ativo', Boolean, nullable=False)

    perfil_id = Column(Integer, ForeignKey('perfil.id'), nullable=False)

    perfil = relationship("PerfilModel", back_populates="usuarios", lazy="joined", foreign_keys=[perfil_id])
