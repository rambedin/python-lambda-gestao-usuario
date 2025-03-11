import logging

from sqlalchemy.exc import SQLAlchemyError

from src.adapters.mysql.models.usuario_notificacao_model import UsuarioNotificacaoModel
from src.util.get_session_db import get_session_db

logger = logging.getLogger(__name__)

class UsuarioNotificacaoRepository:

    def __init__(self):
        self.session = get_session_db()

    def obter_por_dominio_usuario(self, dominio_id: str, id: str):
        try:
            print(f"DEBUG: Buscando notificações para dominio_id={dominio_id}, id={id}")

            query = self.session.query(UsuarioNotificacaoModel).filter(
                UsuarioNotificacaoModel.usuario_dominio_id == dominio_id,
                UsuarioNotificacaoModel.usuario_id == id,
                UsuarioNotificacaoModel.lida == False,
                UsuarioNotificacaoModel.ativo == True
            ).order_by(UsuarioNotificacaoModel.data_hora_cadastro.desc())

            result = query.all()
            print(f"DEBUG: Resultado da busca = {result}")

            return result

        except SQLAlchemyError as e:
            self.session.rollback()
            raise Exception(f"Erro ao buscar notificações: {str(e)}")

    #metodo para persistir uma notificações de usuario.
    def salvar(self, entity: UsuarioNotificacaoModel) -> UsuarioNotificacaoModel:
        try:
            logger.info(f"Salvando entidade com ID: {entity.id}")

            self.session.add(entity)
            self.session.flush()  # Garante que os dados são enviados antes do commit
            self.session.commit()

            return entity

        except SQLAlchemyError as e:
            self.session.rollback()  # Evita que a sessão fique corrompida
            logger.error(f"Erro ao salvar entidade: {e}", exc_info=True)
            raise Exception(f"Erro ao salvar a notificação do usuário: {str(e)}")