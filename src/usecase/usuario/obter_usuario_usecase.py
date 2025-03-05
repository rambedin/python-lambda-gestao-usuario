from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository


class ObterUsuarioUsecase:

    def __init__(self):
        self.repository = UsuarioRepository()

    def obter_todos(self, codigo_dominio):
        return self.repository.obter_todos(codigo_dominio)