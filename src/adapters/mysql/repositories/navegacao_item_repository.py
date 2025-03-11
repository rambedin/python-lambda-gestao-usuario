from src.adapters.mysql.models.navegacao_item_model import NavegacaoItemModel
from src.util.get_session_db import get_session_db


class NavegacaoItemRepository:

    def __init__(self):
        self.session = get_session_db()

    def obter_todos(self):
        query = self.session.query(NavegacaoItemModel).where(NavegacaoItemModel.ativo == 1, NavegacaoItemModel.navegacao_item_id == None)
        result = self.session.execute(query)
        return result.scalars()