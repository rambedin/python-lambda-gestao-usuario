from __future__ import annotations  # Permite referências circulares no Pydantic
from pydantic import BaseModel, Field
from typing import Optional, List

class NavegacaoItem(BaseModel):
    id: int
    titulo: str
    tipo: str
    icone: Optional[str] = None
    link: Optional[str] = None
    ordem: int
    ativo: bool
    navegacao_item_id: Optional[int] = None

    itens: List["NavegacaoItem"] = Field(default_factory=list)  # Correção da referência recursiva

    class Config:
        from_attributes = True  # Substitui orm_mode no Pydantic v2
