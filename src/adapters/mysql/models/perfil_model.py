from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.util.base_declarative import Base

class PerfilModel(Base):
    __tablename__ = "perfil"

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column('nome', String(45), nullable=False)
    tag = Column('tag', String(45), nullable=False)

    usuarios = relationship("UsuarioModel", back_populates="perfil")
