from src.adapters.mysql.models.dominio_model import DominioModel
from src.util.get_session_db import session_scope


class DominioRepository:

    def obter_todos(self):
        with session_scope() as session:
            return self.session.query(DominioModel).all()