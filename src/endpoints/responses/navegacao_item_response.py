from typing import Optional

from pydantic import BaseModel


class NavegacaoItemResponse(BaseModel):
    id: int
    title: str
    type: str
    icon: Optional[str] = None
    link: Optional[str] = None