from src.adapters.mysql.models.usuario_model import UsuarioModel
from src.util.get_session_db import get_session_db


class UsuarioRepository:

    def __init__(self):
        self.session = get_session_db()

    #metodo para autenticação do usuario.
    def obter_por_email_e_senha(self, email, senha, ativo=1):
        query = self.session.query(UsuarioModel).where(UsuarioModel.email == email, UsuarioModel.senha == senha, UsuarioModel.ativo == ativo)
        result = self.session.execute(query)
        return result.scalars().first()

    def obter_todos(self, dominio_id: str):
        query = self.session.query(UsuarioModel).where(UsuarioModel.dominio_id == dominio_id)
        result = self.session.execute(query)
        return result.scalars()

    def obter_por_codigo_usuario(self, id):
        query = self.session.query(UsuarioModel).where(UsuarioModel.id == id)
        result = self.session.execute(query)
        return result.scalars().first()

    def obter_por_email(self, email):
        query = self.session.query(UsuarioModel).where(UsuarioModel.email == email)
        result = self.session.execute(query)
        return result.scalars().first()