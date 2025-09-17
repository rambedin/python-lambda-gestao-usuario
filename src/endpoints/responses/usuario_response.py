from typing import Optional
from pydantic import BaseModel
from src.endpoints.responses.perfil_response import PerfilResponse


class UsuarioResponse(BaseModel):
    id: str
    nome: str
    email: str
    avatar: Optional[str] = None

    perfil: Optional[PerfilResponse] = None

    ativo: bool

    # Permite converter diretamente de SQLAlchemy
    model_config = {"from_attributes": True}