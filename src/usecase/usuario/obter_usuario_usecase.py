from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository
from src.domain.models.perfil import Perfil
from src.domain.models.usuario import Usuario

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
            raise(f"Nenhum usuário encontrado com o código: {id}")

        usuario = Usuario(
            id=obj.id,
            nome=obj.nome,
            dominio_id=obj.dominio_id,
            email=obj.email,
            ativo=obj.ativo,
            perfil=Perfil(id=obj.perfil.id, nome=obj.perfil.nome, tag=obj.perfil.tag)
        )

        return usuario

    def obter_por_email(self, email: str):

        obj = self.repository.obter_por_email(email)

        if obj is None:
            raise(f"Nenhum usuário encontrado com o email: {email}")

        return obj
