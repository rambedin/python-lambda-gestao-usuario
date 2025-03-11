from src.adapters.mysql.models.usuario_model import UsuarioModel
from src.util.get_session_db import get_session_db
from sqlalchemy.exc import SQLAlchemyError

class UsuarioRepository:

    def __init__(self):
        self.session = get_session_db()

    def obter_por_email_e_senha(self, email, senha, ativo=1):
        try:
            usuario = self.session.query(UsuarioModel).filter(
                UsuarioModel.email == email,
                UsuarioModel.senha == senha,
                UsuarioModel.ativo == ativo
            ).first()

            if usuario:
                return usuario

            return None

        except SQLAlchemyError as e:
            self.session.rollback()
            raise Exception(f"Erro ao autenticar usuário: {str(e)}")

    def obter_todos(self, dominio_id: str):
        try:
            return self.session.query(UsuarioModel).filter(
                UsuarioModel.dominio_id == dominio_id
            ).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise Exception(f"Erro ao buscar usuários: {str(e)}")

    def obter_por_codigo_usuario(self, id):
        try:
            return self.session.query(UsuarioModel).filter(
                UsuarioModel.id == id
            ).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise Exception(f"Erro ao buscar usuário por código: {str(e)}")

    def obter_por_email(self, email):
        try:
            return self.session.query(UsuarioModel).filter(
                UsuarioModel.email == email
            ).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise Exception(f"Erro ao buscar usuário por email: {str(e)}")

    def fechar_sessao(self):
        self.session.close()
