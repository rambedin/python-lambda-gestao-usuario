from typing import Optional

from pydantic import BaseModel, field_validator


class Usuario(BaseModel):

    id: str
    dominio_id: str

    nome: str

    @field_validator('nome')
    def validate_nome(cls, nome):
        if not nome:
            raise ValueError("Nome nao pode ser vazio")
        if len(nome) < 3:
            raise ValueError("Nome nao pode ter menos que 3 caracteres")
        return nome

    email: str
    senha: Optional[str] = None
    role: Optional[str] = None

    ativo: bool