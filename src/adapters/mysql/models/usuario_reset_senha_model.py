import datetime
import uuid

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy_utils import UUIDType

from src.util.base_declarative import Base


class UsuarioResetSenhaModel(Base):

    __tablename__ = 'usuario_recuperacao_senha'

    id = Column('id', String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))

    usuario_id = Column('usuario_id', String(36), ForeignKey('usuario.id'), nullable=False)
    usuario_dominio_id  = Column('usuario_dominio_id', String(36), ForeignKey('usuario.dominio_id'), nullable=False)

    token = Column('token', String(255), nullable=False)  # Garante que sempre haja um token
    data_hora_expiracao = Column('data_hora_expiracao', DateTime, nullable=False, default=lambda: datetime.utcnow())  # Evita NULL e usa UTC
    ativo = Column('ativo', String(1), default=False, nullable=False)  # Usa Boolean para mais segurança
