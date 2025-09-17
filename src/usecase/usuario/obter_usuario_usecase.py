from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository
from src.domain.models.usuario import Usuario
from src.util.logger import logger


class ObterUsuarioUsecase:

    def __init__(self):
        self.repository = UsuarioRepository()

    def obter_todos_paginado(self, dominio_id):
        usuarios_paginados = self.repository.obter_todos_paginado(dominio_id)

        logger.info("Usuários paginados antes da conversão:")
        logger.info(usuarios_paginados)

        return usuarios_paginados

    def obter_todos(self, dominio_id):
        return self.repository.obter_todos(dominio_id)

    def obter_por_codigo_usuario(self, id: str):
        obj = self.repository.obter_por_codigo_usuario(id)
        logger.info(obj)

        if not obj:
            raise Exception(f"Nenhum usuário encontrado com o id: {id}")  # ✅ Corrigido `raise`

        return obj

    def obter_por_email(self, email: str):
        obj = self.repository.obter_por_email(email)

        if not obj:
            raise Exception(f"Nenhum usuário encontrado com o email: {email}")  # ✅ Corrigido `raise`

        return obj
