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
async def me(token: dict = Depends(decode_refresh_token)):
    codigo_dominio = token.get('tenant')
    print(f"buscando dentro da contratação: {codigo_dominio}")
    usecase = ObterUsuarioUsecase()
    return usecase.obter_todos(codigo_dominio).all()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    try:

        usuario = authenticate_user(form_data.username, form_data.password)

        access_token = create_token(usuario, "access", 60)
        refresh_token = create_token(usuario, "refresh", 60*24*3)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=403, detail="Usuário ou senha inválidos")

@router.post("/token/refresh")
async def refresh_access_token(token: dict = Depends(decode_refresh_token)):

    #user = get_user(token.get["sub"]) # arbitrary function to get user by email

    user = obter_por_codigo(token.get["sub"])

    access_token = create_token(user, "access", 60)
    refresh_token = create_token(user, "refresh", 60*24*3)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

async def obter_por_codigo(codigo_usuario, codigo_dominio):
    return {"codigo_usuario":"8792e198-f962-11ef-a93d-6045cb9e8621", "codigo_dominio":"18c156d8-f960-11ef-a93d-6045cb9e8621", "email":"rbedin.alencar@gmail.com"}