from pydantic import BaseModel


class NotificacaoRequest(BaseModel):
    id: str