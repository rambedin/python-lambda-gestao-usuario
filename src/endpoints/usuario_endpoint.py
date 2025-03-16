from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

from src.endpoints.responses.usuario_response import UsuarioResponse
from src.usecase.usuario.obter_usuario_usecase import ObterUsuarioUsecase
from src.util.auth import decode_refresh_token
from src.util.logger import logger


router = APIRouter()

@router.get("/me")
async def me(token: dict = Depends(decode_refresh_token)):
    try:
        usecase = ObterUsuarioUsecase()
        return usecase.obter_por_codigo_usuario(token.get('sub')) #sub = codigo_usuario no token
    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel obter as informações do usuário.")

@router.get("", response_model=Page[UsuarioResponse])
async def obter_todos(token: dict = Depends(decode_refresh_token)):
    try:
        dominio_id = token.get('tenant')

        usecase = ObterUsuarioUsecase()
        paginacao = usecase.obter_todos_paginado(dominio_id)

        def map_to_response(item):
            return UsuarioResponse(
                id=item.id,
                nome=item.nome,
                email=item.email
            )

        paginacao.items = [map_to_response(i) for i in paginacao.items]

        logger.info(f"listando usuarios para o dominio: {dominio_id}")

        return Page[UsuarioResponse](
            items=paginacao.items,
            total=paginacao.total,
            page=paginacao.page,
            size=paginacao.size,
            pages=paginacao.pages
        )

    except Exception as e:
        logger.error(f"Erro ao obter usuários: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Não foi possível obter a lista de usuários.")
