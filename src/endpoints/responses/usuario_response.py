from pydantic import BaseModel

class UsuarioResponse(BaseModel):
    id: str
    nome: str
    email: str