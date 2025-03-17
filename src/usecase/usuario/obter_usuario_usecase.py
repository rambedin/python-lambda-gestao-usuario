from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository

class ObterUsuarioUsecase:

    def __init__(self):
        self.repository = UsuarioRepository()

    def obter_todos_paginado(self, dominio_id):
        return self.repository.obter_todos_paginado(dominio_id)

    def obter_todos(self, dominio_id):
        return self.repository.obter_todos(dominio_id)

    def obter_por_codigo_usuario(self, id: str):

        obj = self.repository.obter_por_codigo_usuario(id)

        if obj is None:
            raise(f"Nenhum usuário encontrado com o id: {id}")

        return obj

    def obter_por_email(self, email: str):

        obj = self.repository.obter_por_email(email)

        if obj is None:
            raise(f"Nenhum usuário encontrado com o email: {email}")

        return obj
