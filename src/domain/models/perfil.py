from pydantic import BaseModel

class Perfil(BaseModel):
    id: int
    nome: str
    tag: str