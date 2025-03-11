import datetime

from src.adapters.mysql.models.usuario_notificacao_model import UsuarioNotificacaoModel
from src.adapters.mysql.repositories.usuario_notificacao_repository import UsuarioNotificacaoRepository
from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository

class AuthUsuarioUsecase:

    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def auth(self, email, senha):

        entity = self.usuario_repository.obter_por_email_e_senha(email, senha)

        if entity:
            
            entity_notificacao = UsuarioNotificacaoModel()
            entity_notificacao.usuario_id = entity.id
            entity_notificacao.usuario_dominio_id = entity.dominio_id
            entity_notificacao.titulo = "Login"
            entity_notificacao.descricao = "Realizou login na plataforma de eventos."
            entity_notificacao.icone = "heroicons_mini:star"

            notificacao_repository = UsuarioNotificacaoRepository()
            notificacao_repository.salvar(entity_notificacao)

        return entity
