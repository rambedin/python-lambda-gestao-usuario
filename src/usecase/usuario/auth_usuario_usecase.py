from src.adapters.mysql.repositories.usuario_repository import UsuarioRepository

class AuthUsuarioUsecase:

    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def auth(self, email, senha):
        return self.usuario_repository.obter_por_email_e_senha(email, senha)
