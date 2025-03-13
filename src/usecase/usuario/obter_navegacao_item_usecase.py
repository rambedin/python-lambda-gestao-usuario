import logging
from typing import List

from src.adapters.mysql.repositories.navegacao_item_repository import NavegacaoItemRepository

logger = logging.getLogger(__name__)

class ObterNavegacaoItemUsecase:

    def __init__(self):
        self.repository = NavegacaoItemRepository()

    def obter_todos(self) -> List[dict]:

        """Obtém todos os itens do menu e os organiza em estrutura hierárquica."""
        try:
            # Busca todos os itens do banco (já convertidos para Pydantic)
            itens = self.repository.obter_todos()

            logger.info("Realizando a montagem da hierarquia de navegação.")

            # Criar um dicionário onde a chave é o ID do item
            menu_dict = {item.id: item.model_dump(mode="json") for item in itens}

            # Garantir que todos os itens tenham um array 'itens' para submenus
            for item in menu_dict.values():
                item.setdefault("itens", [])

            menu_tree = []

            for item in itens:
                if item.navegacao_item_id:
                    # Se o item tem um pai, adiciona como subitem
                    menu_dict[item.navegacao_item_id]["itens"].append(menu_dict[item.id])
                else:
                    # Se não tem pai, é um item raiz do menu
                    menu_tree.append(menu_dict[item.id])

            logger.info("Hierarquia montada com sucesso.")
            logger.debug(menu_tree)  # Log detalhado da estrutura final

            return menu_tree

        except Exception as e:
            logger.error(f"Erro ao montar a hierarquia do menu: {str(e)}")
            raise Exception(f"Erro ao montar a hierarquia do menu: {str(e)}")
