import uuid

from sqlalchemy import Column, String, DATETIME, ForeignKey

from src.util.base_declarative import Base


class UsuarioNotificacaoModel(Base):

    __tablename__ = "usuario_notificacao"

    id = Column('id', String(36), primary_key=True, index=True, nullable=False, default=uuid.uuid4())
    usuario_id = Column('usuario_id', String(36), ForeignKey("usuario.id"), nullable=False)
    usuario_dominio_id = Column('usuario_dominio_id', String(36), ForeignKey("usuario.dominio_id"), nullable=False)
    icone = Column('icone', String(30))
    titulo = Column('titulo', String(30))
    descricao = Column('descricao', String(120))
    data_hora_cadastro = Column('data_hora_cadastro', DATETIME, nullable=True)
    link = Column('link', String(60))
    e_rota = Column('e_rota', String(1))
    ativo = Column('ativo', String(1))
