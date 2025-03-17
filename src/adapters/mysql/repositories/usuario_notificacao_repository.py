from sqlalchemy.exc import SQLAlchemyError

from src.adapters.mysql.models.usuario_notificacao_model import UsuarioNotificacaoModel
from src.domain.models.usuario_notificacao import UsuarioNotificacao
from src.util.get_session_db import session_scope
from src.util.logger import logger


class UsuarioNotificacaoRepository:

    def obter_por_codigo_notificacao(self, id: str) -> UsuarioNotificacao:
        try:

            logger.info(f"Buscando notificação com código: {id}")

            with session_scope() as session:

                notificacao = session.query(UsuarioNotificacaoModel).filter(
                    UsuarioNotificacaoModel.id == id
                ).first()

                logger.info(f"Resultado da busca = {notificacao}")

                if not notificacao:
                    return None

                return UsuarioNotificacao.model_validate({**notificacao.__dict__, "dominio_id": notificacao.usuario_dominio_id})

        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar notificação: {str(e)}")

    def obter_por_dominio_usuario(self, dominio_id: str, id: str):
        try:
            logger.info(f"Buscando notificações para dominio_id={dominio_id}, id={id}")

            with session_scope() as session:

                query = session.query(UsuarioNotificacaoModel).filter(
                    UsuarioNotificacaoModel.usuario_dominio_id == dominio_id,
                    UsuarioNotificacaoModel.usuario_id == id,
                    UsuarioNotificacaoModel.ativo == True
                ).order_by(UsuarioNotificacaoModel.data_hora_cadastro.desc())

                notificacoes = query.all()

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

    #--------------------------------------------------------------------------------------------------------
    # metodo para persistir uma notificações de usuario.
    #--------------------------------------------------------------------------------------------------------
    def salvar(self, entity: UsuarioNotificacaoModel) -> UsuarioNotificacaoModel:
        try:

            with session_scope() as session:
                session.add(entity)
                session.flush()
                session.commit()

            logger.info(f"Notificação salva com sucesso!")

            return entity

        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f"Erro ao salvar entidade: {e}", exc_info=True)
            raise Exception(f"Erro ao salvar a notificação do usuário: {str(e)}")

    #--------------------------------------------------------------------------------------------------------
    # metodo para atualizar uma notificações de usuario.
    #--------------------------------------------------------------------------------------------------------
    def atualizar(self, domain: UsuarioNotificacao) -> UsuarioNotificacao:
        try:

            with session_scope() as session:

                session.query(UsuarioNotificacaoModel).filter(UsuarioNotificacaoModel.id == domain.id).update({
                    UsuarioNotificacaoModel.lida: domain.lida,
                    UsuarioNotificacaoModel.ativo: domain.ativo
                }, synchronize_session='fetch')

                session.commit()

                logger.info(f"Notificação atualizada com sucesso!")

                notificacao_atualizada = session.query(UsuarioNotificacaoModel).filter(
                    UsuarioNotificacaoModel.id == domain.id
                ).first()

                return UsuarioNotificacao.model_validate({
                    **notificacao_atualizada.__dict__,
                    "dominio_id": notificacao_atualizada.usuario_dominio_id
                })

        except SQLAlchemyError as e:
            logger.error(f"Erro ao atualizar entidade: {e}", exc_info=True)
            raise Exception(f"Erro ao atualizar a notificação do usuário: {str(e)}")