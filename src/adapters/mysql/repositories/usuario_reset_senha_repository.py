from src.adapters.mysql.models.usuario_notificacao_model import UsuarioNotificacaoModel
from src.util.get_session_db import get_session_db


class UsuarioResetSenhaRepository:

    def __init__(self):
        self.session = get_session_db()

    #metodo para obter as notificações do usuario.
    def salvar(self, entity: UsuarioNotificacaoModel):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)