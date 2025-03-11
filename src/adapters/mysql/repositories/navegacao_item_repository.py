from src.adapters.mysql.models.navegacao_item_model import NavegacaoItemModel
from src.util.get_session_db import session_scope

class NavegacaoItemRepository:

    def obter_todos(self):
        with session_scope() as session:
            query = session.query(NavegacaoItemModel).filter(
                NavegacaoItemModel.ativo == 1,
                NavegacaoItemModel.navegacao_item_id.is_(None)  # Comparação correta com NULL
            )
            return query.all()  # Retorna diretamente os resultados
