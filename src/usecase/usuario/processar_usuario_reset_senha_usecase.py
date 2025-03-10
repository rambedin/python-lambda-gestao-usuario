import secrets
from datetime import timedelta, datetime

from src.adapters.mysql.models.usuario_reset_senha_model import UsuarioResetSenhaModel
from src.adapters.mysql.repositories.usuario_reset_senha_repository import UsuarioResetSenhaRepository
from src.usecase.usuario.obter_usuario_usecase import ObterUsuarioUsecase


class ProcessarUsuarioResetSenhaUsecase:

    def __init__(self):
        self.repository = UsuarioResetSenhaRepository()

    def processar_usuario_reset_senha(self, email):

        try:

            usecase = ObterUsuarioUsecase()
            usuario = usecase.obter_por_email(email)

            token = secrets.token_urlsafe(32)
            data_hora_expiracao = datetime.utcnow() + timedelta(hours=1) #expira em 1 hora.

            entity = UsuarioResetSenhaModel()
            entity.usuario_id = usuario.id
            entity.usuario_dominio_id = usuario.dominio_id
            entity.token = token
            entity.data_hora_expiracao = data_hora_expiracao
            entity.ativo = 1

            print(entity.usuario_id)
            print(entity.usuario_dominio_id)
            print(entity.token)
            print(entity.data_hora_expiracao)
            print(entity.ativo)

            self.repository.salvar(entity)


        except Exception as e:
            print(e)
            raise(e)