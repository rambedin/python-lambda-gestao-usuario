from pydantic import BaseModel

class PerfilResponse(BaseModel):
    id: int
    nome: str