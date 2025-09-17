from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.exc import SQLAlchemyError
from src.adapters.mysql.models.usuario_model import UsuarioModel
from src.domain.models.usuario import Usuario
from src.util.get_session_db import session_scope
from src.util.logger import logger


class UsuarioRepository:

    def obter_todos_paginado(self, dominio_id: str):
        try:
            with session_scope() as session:

                query = session.query(UsuarioModel).filter(UsuarioModel.dominio_id == dominio_id)

                logger.info('Aplicando o paginate...')
                usuarios_paginados = paginate(query)  # ✅ `paginate()` já retorna uma lista

                logger.info(f'Usuários paginados: {usuarios_paginados.items}')
                return usuarios_paginados  # ✅ Retorna objetos `UsuarioModel` sem conversão inesperada
        except SQLAlchemyError as e:
            logger.error(f"Erro ao buscar usuários: {str(e)}", exc_info=True)
            raise Exception(f"Erro ao buscar usuários: {str(e)}")

    def obter_por_email_e_senha(self, email, senha, ativo=1) -> Usuario:
        try:
            with session_scope() as session:
                usuario = session.query(UsuarioModel).filter(
                    UsuarioModel.email == email,
                    UsuarioModel.senha == senha,
                    UsuarioModel.ativo == ativo
                ).first()

                if not usuario:
                    return None  #  Retorna None explicitamente se o usuário não for encontrado

                return Usuario.model_validate(usuario.to_domain())  # model_validate() já pode lidar com SQLAlchemy
        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f"Erro ao autenticar usuário: {str(e)}", exc_info=True)
            raise Exception(f"Erro ao autenticar usuário: {str(e)}")

    def obter_por_codigo_usuario(self, id):
        try:
            with session_scope() as session:
                usuario = session.query(UsuarioModel).filter(
                    UsuarioModel.id == id,
                    UsuarioModel.ativo == True
                ).first()

                if not usuario:
                    raise Exception(f'Usuário não encontrado com a id: {id}')  # Corrigido `raise Exception(...)`

                return Usuario.model_validate(usuario.to_domain())  # `model_validate()` converte SQLAlchemy diretamente
        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f"Erro ao buscar usuário por código: {str(e)}", exc_info=True)
            raise Exception(f"Erro ao buscar usuário por código: {str(e)}")

    def obter_por_email(self, email):
        try:
            with session_scope() as session:
                return session.query(UsuarioModel).filter(
                    UsuarioModel.email == email
                ).first()
        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f"Erro ao buscar usuário por email: {str(e)}", exc_info=True)
            raise Exception(f"Erro ao buscar usuário por email: {str(e)}")
