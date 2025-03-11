import secrets
import logging
from datetime import timedelta, datetime

from src.adapters.mysql.models.usuario_reset_senha_model import UsuarioResetSenhaModel
from src.adapters.mysql.repositories.usuario_reset_senha_repository import UsuarioResetSenhaRepository
from src.usecase.usuario.obter_usuario_usecase import ObterUsuarioUsecase

# Configuração do logger para registrar erros
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class ProcessarUsuarioResetSenhaUsecase:
    def __init__(self):
        self.repository = UsuarioResetSenhaRepository()

    def processar_usuario_reset_senha(self, email):
        try:
            usecase = ObterUsuarioUsecase()
            usuario = usecase.obter_por_email(email)

            if not usuario:
                raise ValueError("Usuário não encontrado para o e-mail informado.")

            token = secrets.token_urlsafe(32)
            data_hora_expiracao = datetime.utcnow() + timedelta(hours=1)  # Expira em 1 hora

            entity = UsuarioResetSenhaModel(
                usuario_id=usuario.id,
                usuario_dominio_id=usuario.dominio_id,
                token=token,
                data_hora_expiracao=data_hora_expiracao,
                ativo=1
            )

            print(f"Usuário ID: {entity.usuario_id}")
            print(f"Domínio ID: {entity.usuario_dominio_id}")
            print(f"Token: {entity.token}")
            print(f"Expiração: {entity.data_hora_expiracao}")
            print(f"Ativo: {entity.ativo}")

            self.repository.salvar(entity)

        except Exception as e:
            logger.error(f"Erro ao processar reset de senha: {str(e)}", exc_info=True)
            raise
