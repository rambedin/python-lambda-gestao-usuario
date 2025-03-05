from sqlalchemy import Column, String, DATETIME
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DominioModel(Base):

    __tablename__ = "dominio"

    codigo_dominio = Column(String(36), primary_key=True, index=True)