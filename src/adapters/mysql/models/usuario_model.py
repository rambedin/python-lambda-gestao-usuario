import uuid

from sqlalchemy import Column, String, ForeignKey

from src.util.base_declarative import Base


class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column('id', String(36), primary_key=True, nullable=False, default=uuid.uuid4())
    dominio_id = Column('dominio_id', String(36), ForeignKey('dominio.id'), primary_key=True, nullable=False)
    nome = Column('nome', String(120), nullable=False)
    email = Column('email', String(70), nullable=False)
    senha = Column('senha', String(72), nullable=False)
    ativo = Column('ativo', String(1), nullable=False)
