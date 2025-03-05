from src.adapters.mysql.models.usuario_model import UsuarioModel
from src.util.get_session_db import get_session_db


class UsuarioRepository:

    def __init__(self):
        self.session = get_session_db()

    #metodo para autenticação do usuario.
    def obter_por_email_e_senha(self, email, senha):
        query = self.session.query(UsuarioModel).where(UsuarioModel.email == email, UsuarioModel.senha == senha)
        result = self.session.execute(query)
        return result.scalars().first()

    def obter_todos(self, codigo_dominio: str):
        query = self.session.query(UsuarioModel).where(UsuarioModel.codigo_dominio == codigo_dominio)
        result = self.session.execute(query)
        return result.scalars()

    def obter_por_codigo_usuario(self, codigo_usuario):
        query = self.session.query(UsuarioModel).where(UsuarioModel.codigo_usuario == codigo_usuario)
        result = self.session.execute(query)
        return result.scalars().first()