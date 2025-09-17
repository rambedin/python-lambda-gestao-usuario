from typing import Optional
from pydantic import BaseModel, field_validator, EmailStr

from src.domain.models.dominio import Dominio
from src.domain.models.perfil import Perfil


class Usuario(BaseModel):

    # Atributos Base
    id: str
    dominio_id: str
    nome: str
    email: EmailStr
    senha: Optional[str] = None
    role: Optional[str] = None
    ativo: bool

    # Relacionamentos
    dominio: Optional[Dominio] = None
    perfil: Optional[Perfil] = None

    # Configuração para aceitar objetos SQLAlchemy automaticamente
    model_config = {"from_attributes": True}  # ✅ Permite receber `UsuarioModel` diretamente
