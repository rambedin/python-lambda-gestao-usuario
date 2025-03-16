from src.util.get_session_db import session_scope
from sqlalchemy.exc import SQLAlchemyError
from fastapi_pagination.ext.sqlalchemy import paginate
from src.domain.models.usuario import Usuario
from src.adapters.mysql.models.usuario_model import UsuarioModel

class UsuarioRepository:

    def obter_por_email_e_senha(self, email, senha, ativo=1) -> Usuario:
        try:

            with session_scope() as session:
                usuario = session.query(UsuarioModel).filter(
                    UsuarioModel.email == email,
                    UsuarioModel.senha == senha,
                    UsuarioModel.ativo == ativo
                ).first()

                if not usuario:
                    return None

                return Usuario.model_validate(usuario.__dict__)

        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Erro ao autenticar usuário: {str(e)}")

    def obter_todos_paginado(self, dominio_id: str):
        try:
            with session_scope() as session:
                query = session.query(UsuarioModel).filter(UsuarioModel.dominio_id == dominio_id)
                return paginate(query)
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar usuários: {str(e)}")

    def obter_todos(self, dominio_id: str) -> list[Usuario]:
        """Obtém todos os usuários de um domínio e retorna uma lista de Pydantic"""
        try:
            with session_scope() as session:  # ✅ Corrigido: session_scope() precisa de ()
                usuarios = session.query(UsuarioModel).filter(
                    UsuarioModel.dominio_id == dominio_id
                ).all()

                if not usuarios:
                    return []  # ✅ Retorna lista vazia se não encontrar usuários

                # Converte lista de SQLAlchemy Models para lista de Pydantic Models
                return [Usuario.model_validate(usuario.__dict__) for usuario in usuarios]  # ✅ Conversão para Pydantic
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao buscar usuários: {str(e)}")

    def obter_por_codigo_usuario(self, id):
        try:
            with session_scope() as session:
                return session.query(UsuarioModel).filter(
                    UsuarioModel.id == id
                ).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Erro ao buscar usuário por código: {str(e)}")

    def obter_por_email(self, email):
        try:
            with session_scope() as session:
                return session.query(UsuarioModel).filter(
                    UsuarioModel.email == email
                ).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Erro ao buscar usuário por email: {str(e)}")