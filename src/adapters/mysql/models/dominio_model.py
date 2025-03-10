import uuid

from sqlalchemy import Column, String

from src.util.base_declarative import Base


class DominioModel(Base):

    __tablename__ = 'dominio'

    codigo_dominio = Column('id', String(36), primary_key=True, index=True, nullable=False, default=uuid.uuid4())