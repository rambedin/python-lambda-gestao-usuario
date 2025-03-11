from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class NotificacaoResponse(BaseModel):
    id: str  # UUIDs são strings
    icon: Optional[str] = None
    title: str
    description: str
    time: datetime
    read: bool = False  # Define um valor padrão
    link: Optional[str] = None
    useRouter: bool
