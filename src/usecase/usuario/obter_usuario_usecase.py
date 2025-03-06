from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository
from src.domain.models.usuario import Usuario

class ObterUsuarioUsecase:

    def __init__(self):
        self.repository = UsuarioRepository()

    def obter_todos(self, codigo_dominio):
        return self.repository.obter_todos(codigo_dominio)

    def obter_por_codigo_usuario(self, codigo_usuario: str):

        obj = self.repository.obter_por_codigo_usuario(codigo_usuario)

        if obj is None:
            raise("Nenhum usuário encontrado.")

        usuario = Usuario()
        usuario.codigo_usuario = obj.codigo_usuario
        usuario.codigo_dominio = obj.codigo_dominio
        usuario.email = obj.email

        return usuario