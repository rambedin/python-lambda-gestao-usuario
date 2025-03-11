import logging

from sqlalchemy.exc import SQLAlchemyError

from src.adapters.mysql.models.usuario_notificacao_model import UsuarioNotificacaoModel
from src.domain.models.usuario_notificacao import UsuarioNotificacao
from src.util.get_session_db import session_scope

logger = logging.getLogger(__name__)

class UsuarioNotificacaoRepository:


    def obter_por_dominio_usuario(self, dominio_id: str, id: str):
        try:
            print(f"DEBUG: Buscando notificações para dominio_id={dominio_id}, id={id}")

            with session_scope() as session:

                query = session.query(UsuarioNotificacaoModel).filter(
                    UsuarioNotificacaoModel.usuario_dominio_id == dominio_id,
                    UsuarioNotificacaoModel.usuario_id == id,
                    UsuarioNotificacaoModel.lida == False,
                    UsuarioNotificacaoModel.ativo == True
                ).order_by(UsuarioNotificacaoModel.data_hora_cadastro.desc())

                notificacoes = query.all()

                print(f"DEBUG: Resultado da busca = {notificacoes}")

                if not notificacoes:
                    return []

                return [
                    UsuarioNotificacao.model_validate({
                        **notificacao.__dict__,
                        "dominio_id": notificacao.usuario_dominio_id
                    }) for notificacao in notificacoes
                ]

        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Erro ao buscar notificações: {str(e)}")

    #metodo para persistir uma notificações de usuario.
    def salvar(self, entity: UsuarioNotificacaoModel) -> UsuarioNotificacaoModel:
        try:

            logger.info(f"Salvando entidade com ID: {entity.id}")

            with session_scope() as session:
                session.add(entity)
                session.flush()  # Garante que os dados são enviados antes do commit
                session.commit()

            return entity

        except SQLAlchemyError as e:
            session.rollback()  # Evita que a sessão fique corrompida
            logger.error(f"Erro ao salvar entidade: {e}", exc_info=True)
            raise Exception(f"Erro ao salvar a notificação do usuário: {str(e)}")