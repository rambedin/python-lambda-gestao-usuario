import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, func
from src.util.base_declarative import Base

class UsuarioNotificacaoModel(Base):
    __tablename__ = "usuario_notificacao"

    id = Column(String(36), primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    usuario_id = Column(String(36), ForeignKey("usuario.id"), nullable=False)
    usuario_dominio_id = Column(String(36), ForeignKey("usuario.dominio_id"), nullable=False)

    icone = Column(String(30), nullable=True)
    titulo = Column(String(30))
    descricao = Column(String(120))
    data_hora_cadastro = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    link = Column(String(60), nullable=True)
    e_rota = Column(Boolean, nullable=False, default=False)
    lida = Column(Boolean, nullable=False, default=False)
    ativo = Column(Boolean, nullable=False, default=True)
