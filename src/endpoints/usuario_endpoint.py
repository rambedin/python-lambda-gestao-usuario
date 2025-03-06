from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.usecase.usuario.obter_usuario_usecase import ObterUsuarioUsecase
from src.util.auth import authenticate_user, create_token, decode_refresh_token

router = APIRouter()

@router.get("/me")
async def me(token: dict = Depends(decode_refresh_token)):
    try:
        usecase = ObterUsuarioUsecase()
        return usecase.obter_por_codigo_usuario(token.get('sub')) #sub = codigo_usuario no token
    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel obter as informações do usuário.")

@router.get("")
async def obter_todos(token: dict = Depends(decode_refresh_token)):
    codigo_dominio = token.get('tenant')
    print(f"buscando dentro da contratação: {codigo_dominio}")
    usecase = ObterUsuarioUsecase()
    return usecase.obter_todos(codigo_dominio).all()