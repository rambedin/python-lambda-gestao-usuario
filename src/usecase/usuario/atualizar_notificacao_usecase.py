
from src.adapters.mysql.repositories.usuario_notificacao_repository import UsuarioNotificacaoRepository
from sqlalchemy.exc import SQLAlchemyError

from src.util.logger import logger


class AtualizarNotificacaoUsecase:

    def __init__(self):
        self.repository = UsuarioNotificacaoRepository()

    def atualizar_por_codigo_notificacao(self, id):
        try:

            notificaco = self.repository.obter_por_codigo_notificacao(id)

            if not notificaco:
                raise Exception(f"Não foi localizada a notificação: {id}")

            if not notificaco.lida:
                notificaco.lida = True
            else:
                notificaco.lida = False

            return self.repository.atualizar(notificaco)

        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar notificações: {str(e)}")

    def excluir_por_codigo_notificacao(self, id):
        try:

            notificaco = self.repository.obter_por_codigo_notificacao(id)

            if not notificaco:
                raise Exception(f"Não foi localizada a notificação: {id}")

            notificaco.ativo = False

            return self.repository.atualizar(notificaco)

        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar notificações: {str(e)}")
