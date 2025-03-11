import logging

from fastapi import APIRouter, Depends, HTTPException

from src.endpoints.responses.navegacao_item_response import NavegacaoItemResponse
from src.usecase.usuario.obter_navegacao_item_usecase import ObterNavegacaoItemUsecase
from src.util.auth import decode_refresh_token

router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("")
async def obter_todos(token: dict = Depends(decode_refresh_token)):
    try:
        usecase = ObterNavegacaoItemUsecase()

        data = [
            NavegacaoItemResponse(
                id=row.id,
                title=row.titulo,
                type=row.tipo,
                icon=row.icone,
                link=row.link
            )
            for row in usecase.obter_todos()
        ]

        return {
            "compact": data,
            "default": data,
            "futuristic": data,
            "horizontal": data
        }

    except Exception as e:
        logger.error(f"Erro ao obter informações de navegação: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Não foi possível obter as informações de navegação.")