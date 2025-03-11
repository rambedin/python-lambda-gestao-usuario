from sqlalchemy.exc import SQLAlchemyError

from src.adapters.mysql.models.usuario_notificacao_model import UsuarioNotificacaoModel
from src.util.get_session_db import session_scope


class UsuarioResetSenhaRepository:

    #metodo para obter as notificações do usuario.
    def salvar(self, entity: UsuarioNotificacaoModel):
        try:
            with session_scope() as session:
                session.add(entity)
                session.commit()
                session.refresh(entity)
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao salvar recuperação de senha : {str(e)}")
