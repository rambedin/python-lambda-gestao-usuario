from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UsuarioModel(Base):

    __tablename__ = "usuario"

    codigo_usuario = Column(String(36), primary_key=True, index=True)
    codigo_dominio = Column(String(36), ForeignKey("dominio.codigo_dominio"), nullable=False)
    email = Column(String(70), nullable=False)
    senha = Column(String(72), nullable=False)