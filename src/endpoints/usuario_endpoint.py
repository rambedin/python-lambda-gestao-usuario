from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

from src.endpoints.responses.perfil_response import PerfilResponse
from src.endpoints.responses.usuario_response import UsuarioResponse
from src.usecase.usuario.obter_usuario_usecase import ObterUsuarioUsecase
from src.util.auth import decode_refresh_token
from src.util.logger import logger

router = APIRouter()

@router.get("/me")
async def me(token: dict = Depends(decode_refresh_token)):
    try:
        usecase = ObterUsuarioUsecase()
        return usecase.obter_por_codigo_usuario(token.get('sub'))  # `sub` = código do usuário no token
    except Exception as e:
        logger.error(f"Erro ao obter usuário: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Não foi possível obter as informações do usuário.")


@router.get("", response_model=Page[UsuarioResponse])
async def obter_todos(token: dict = Depends(decode_refresh_token)):
    try:
        dominio_id = token.get('tenant')

        usecase = ObterUsuarioUsecase()
        usuario_paginados = usecase.obter_todos_paginado(dominio_id)

        def map_to_response(item):
            logger.info(f"Convertendo usuário: {item}")
            return UsuarioResponse(
                id=item.id,
                nome=item.nome,
                email=item.email,
                avatar=f'images/avatars/{item.id}.jpg',
                perfil=PerfilResponse(
                    id=item.perfil.id if item.perfil else None,
                    nome=item.perfil.nome if item.perfil else None
                ) if item.perfil else None,
                ativo=item.ativo
            )

        usuario_paginados.items = [map_to_response(i) for i in usuario_paginados.items]

        logger.info(f"Listando usuários para o domínio: {dominio_id}")

        return Page(
            items=usuario_paginados.items,
            total=usuario_paginados.total,
            page=usuario_paginados.page,
            size=usuario_paginados.size,
            pages=usuario_paginados.pages
        )

    except Exception as e:
        logger.error(f"Erro ao obter usuários: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Não foi possível obter a lista de usuários.")
