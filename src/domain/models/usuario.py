from typing import Optional
from pydantic import BaseModel, field_validator, EmailStr

class Usuario(BaseModel):
    id: str
    dominio_id: str
    nome: str
    email: EmailStr
    senha: Optional[str] = None
    role: Optional[str] = None
    ativo: bool

    @field_validator("nome")
    @classmethod
    def validate_nome(cls, nome: str) -> str:
        if not nome or len(nome) < 3:
            raise ValueError(f"Nome deve ter pelo menos 3 caracteres (atual: {len(nome)})")
        return nome
