from typing import List
from sqlalchemy.exc import SQLAlchemyError

from src.adapters.mysql.models.navegacao_item_model import NavegacaoItemModel
from src.domain.models.navegacao_item import NavegacaoItem
from src.util.get_session_db import session_scope


class NavegacaoItemRepository:

    def obter_todos(self) -> List[NavegacaoItem]:
        try:
            with session_scope() as session:
                query = session.query(NavegacaoItemModel).filter(
                    NavegacaoItemModel.ativo == 1
                )

                itens = query.all()

                # Retorna a lista de objetos Pydantic sem estrutura hierárquica
                return [NavegacaoItem.model_validate(i) for i in itens]

        except SQLAlchemyError as e:
            raise Exception(f"Não foi possível obter os itens de navegação: {str(e)}")
