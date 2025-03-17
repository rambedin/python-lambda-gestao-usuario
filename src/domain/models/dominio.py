from pydantic import BaseModel

class Dominio(BaseModel):
    id: str
    nome: str
    ativo: bool