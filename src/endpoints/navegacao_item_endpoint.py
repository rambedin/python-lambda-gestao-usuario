import logging

from fastapi import APIRouter, Depends, HTTPException

from src.endpoints.responses.navegacao_item_response import NavegacaoItemResponse, NavegacaoItemResponseBadge
from src.usecase.usuario.obter_navegacao_item_usecase import ObterNavegacaoItemUsecase
from src.util.auth import decode_refresh_token

router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("", response_model=dict)
async def obter_todos(token: dict = Depends(decode_refresh_token)):
    try:
        usecase = ObterNavegacaoItemUsecase()
        menu_hierarquico = usecase.obter_todos()

        # Mapeia os dados para `NavegacaoItemResponse`
        def map_to_response(item):
            return NavegacaoItemResponse(
                id=item["id"],
                title=item["titulo"],
                subtitle=item["subtitulo"],
                type=item["tipo"],
                icon=item["icone"],
                link=item["link"],
                badge=NavegacaoItemResponseBadge(
                    title=item["badge_titulo"],
                    classes=item["badge_estilo"]
                ),
                children=[map_to_response(sub) for sub in item["itens"]],
                disabled= not item.get("ativo", False)
            )

        data = [map_to_response(item).dict(exclude_none=True) for item in menu_hierarquico]

        response = {
            "compact": data,
            "default": data,
            "futuristic": data,
            "horizontal": data
        }

        logger.info("Navegação obtida com sucesso.")
        return response

    except Exception as e:
        logger.error(f"Erro ao obter informações de navegação: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Não foi possível obter as informações de navegação.")