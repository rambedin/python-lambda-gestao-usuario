import datetime
from typing import Optional

from pydantic import BaseModel

class UsuarioNotificacao(BaseModel):

    id: Optional[str]
    usuario_id: str
    dominio_id: str
    icone: str
    titulo: str
    descricao: str
    data_hora_cadastro: datetime
    link: Optional[str] = None
    e_rota: bool
    ativo: bool