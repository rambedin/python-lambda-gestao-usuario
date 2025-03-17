import uuid

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from src.util.base_declarative import Base

class DominioModel(Base):

    __tablename__ = "dominio"

    id = Column('id', Integer, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    nome = Column('nome', String(45), nullable=False)
    ativo = Column('ativo', Boolean, nullable=False)

    usuarios = relationship("UsuarioModel", back_populates="dominio")
