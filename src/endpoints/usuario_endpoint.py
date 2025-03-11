from fastapi import APIRouter, Depends, HTTPException

from src.endpoints.responses.notificacao_response import NotificacaoResponse
from src.usecase.usuario.obter_usuario_notificacao_usecase import ObterUsuarioNotificacaoUsecase
from src.usecase.usuario.obter_usuario_usecase import ObterUsuarioUsecase
from src.util.auth import decode_refresh_token

router = APIRouter()

@router.get("/me")
async def me(token: dict = Depends(decode_refresh_token)):
    try:
        usecase = ObterUsuarioUsecase()
        return usecase.obter_por_codigo_usuario(token.get('sub')) #sub = codigo_usuario no token
    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel obter as informações do usuário.")

@router.get("/notificacao")
async def me(token: dict = Depends(decode_refresh_token)):
    try:

        usecase = ObterUsuarioNotificacaoUsecase()

        data = [
            NotificacaoResponse(
                id=row.id,
                icon=row.icone,
                title=row.titulo,
                description=row.descricao,
                time=row.data_hora_cadastro,
                read=row.lida,
                link=row.link,
                useRouter=row.e_rota
            )
            for row in usecase.obter_por_codigo_dominio_usuario(token.get('tenant'), token.get('sub'))
        ]

        return data

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Não foi possivel obter as notificações do usuário.")

@router.get("")
async def obter_todos(token: dict = Depends(decode_refresh_token)):
    try:
        codigo_dominio = token.get('tenant')
        print(f"buscando dentro da contratação: {codigo_dominio}")
        usecase = ObterUsuarioUsecase()
        return usecase.obter_todos(codigo_dominio)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel obter a lista de usuários.")