from src.adapters.mysql.repositories.navegacao_item_repository import NavegacaoItemRepository

class ObterNavegacaoItemUsecase:

    def __init__(self):
        self.repository = NavegacaoItemRepository()

    def obter_todos(self):
        return self.repository.obter_todos()