from pydantic import BaseModel


class UsuarioResetSenhaRequest(BaseModel):
    email: str