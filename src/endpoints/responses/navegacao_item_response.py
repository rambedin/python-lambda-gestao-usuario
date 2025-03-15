from typing import Optional

from pydantic import BaseModel

class NavegacaoItemResponseBadge(BaseModel):
    title: Optional[str] = None
    classes: Optional[str] = None

class NavegacaoItemResponse(BaseModel):

    id: int
    title: str
    subtitle: Optional[str] = None
    type: str
    icon: Optional[str] = None
    link: Optional[str] = None
    children: Optional[list] = None
    badge: Optional[NavegacaoItemResponseBadge] = None
    disabled: bool