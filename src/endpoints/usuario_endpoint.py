from fastapi import APIRouter, Depends, HTTPException

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
        return usecase.obter_por_codigo_dominio_usuario(token.get('tenant'), token.get('sub'))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel obter as notificações do usuário.")

@router.get("")
async def obter_todos(token: dict = Depends(decode_refresh_token)):
    codigo_dominio = token.get('tenant')
    print(f"buscando dentro da contratação: {codigo_dominio}")
    usecase = ObterUsuarioUsecase()
    return usecase.obter_todos(codigo_dominio).all()