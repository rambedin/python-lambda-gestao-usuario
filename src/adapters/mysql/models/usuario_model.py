import uuid
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer
from sqlalchemy.orm import relationship

from src.domain.models.usuario import Usuario
from src.util.base_declarative import Base

# Necessário para o relationship funcionar.
from src.adapters.mysql.models.dominio_model import DominioModel
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

    # Relationships

    dominio = relationship("DominioModel", back_populates="usuarios", lazy="joined", foreign_keys=[dominio_id])
    perfil = relationship("PerfilModel", back_populates="usuarios", lazy="joined", foreign_keys=[perfil_id])

    # Mappers

    def to_dict(self):
        return {
            "id": self.id,
            "dominio_id": self.dominio_id,
            "nome": self.nome,
            "email": self.email,
            "ativo": self.ativo,
            "dominio": {
                "id": self.dominio.id,
                "nome": self.dominio.nome,
                "ativo": self.dominio.ativo
            },
            "perfil": {
                "id": self.perfil.id,
                "nome": self.perfil.nome,
                "tag": self.perfil.tag
            } if self.perfil else None
        }
