from pydantic import BaseModel

from src.endpoints.responses.perfil_response import PerfilResponse


class UsuarioResponse(BaseModel):
    id: str
    nome: str
    email: str

    perfil: PerfilResponse