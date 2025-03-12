from src.adapters.mysql.repositories.usuario_notificacao_repository import UsuarioNotificacaoRepository
from sqlalchemy.exc import SQLAlchemyError

class ObterUsuarioNotificacaoUsecase:

    def __init__(self):
        self.repository = UsuarioNotificacaoRepository()

    def obter_por_codigo_notificacao(self, notificacao_id: str):
        try:
            ds = self.repository.obter_por_codigo_notificacao(notificacao_id)

            if not ds:
                return None

            return ds

        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar notificação: {str(e)}")

    def obter_por_codigo_dominio_usuario(self, dominio_id: str, id: str):
        try:
            ds = self.repository.obter_por_dominio_usuario(dominio_id, id)

            if not ds:  # Se a lista estiver vazia, retorna []
                return []

            return ds

        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar notificações: {str(e)}")
