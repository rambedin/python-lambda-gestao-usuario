from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository


class ObterUsuarioUsecase:

    def __init__(self):
        self.repository = UsuarioRepository()

    def obter_todos(self, codigo_dominio):
        return self.repository.obter_todos(codigo_dominio)

    def obter_por_codigo_usuario(self, codigo_usuario: str):

        usuario = self.repository.obter_por_codigo_usuario(codigo_usuario)

        if usuario is None:
            raise("Nenhum usuário encontrado.")

        return {
            "id": usuario.codigo_usuario,
            "name": "xyz",
            "status": "online",
            "active": 1
        }