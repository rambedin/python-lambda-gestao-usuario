from sqlalchemy import Column, String, Integer, ForeignKey

from src.util.base_declarative import Base


class NavegacaoItemModel(Base):

    __tablename__ = 'navegacao_item'

    id = Column('id', Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    titulo = Column('titulo', String(45), nullable=False)
    subtitulo = Column('subtitulo', String(45), nullable=False)
    tipo = Column('tipo', String(45), nullable=False)
    icone = Column('icone', String(45), nullable=True)
    link = Column('link', String(45), nullable=True)
    badge_titulo = Column('badge_titulo', String(45), nullable=True)
    badge_estilo = Column('badge_estilo', String(45), nullable=True)
    ordem = Column('ordem', Integer, nullable=False, default=0)
    ativo = Column('ativo', Integer, nullable=False, default=1)
    navegacao_item_id = Column('navegacao_item_id', Integer, ForeignKey('navegacao_item.id'), primary_key=True, nullable=False)