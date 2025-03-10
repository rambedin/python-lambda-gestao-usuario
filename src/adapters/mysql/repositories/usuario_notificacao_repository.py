from src.adapters.mysql.models.usuario_notificacao_model import UsuarioNotificacaoModel
from src.util.get_session_db import get_session_db


class UsuarioNotificacaoRepository:

    def __init__(self):
        self.session = get_session_db()

    #metodo para obter as notificações do usuario.
    def obter_por_dominio_usuario(self, dominio_id, id):
        query = self.session.query(UsuarioNotificacaoModel).where(UsuarioNotificacaoModel.usuario_dominio_id == dominio_id, UsuarioNotificacaoModel.id == id)
        result = self.session.execute(query)
        return result.scalars()