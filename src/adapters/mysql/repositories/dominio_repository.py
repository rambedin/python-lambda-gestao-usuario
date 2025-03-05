from src.adapters.mysql.models.dominio_model import DominioModel
from src.util.get_session_db import get_session_db


class DominioRepository:

    def __init__(self):
        self.session = get_session_db()

    def obter_todos(self):
        return self.session.query(DominioModel).all()