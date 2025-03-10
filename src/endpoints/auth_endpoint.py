from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.endpoints.requests.usuario_reset_senha_request import UsuarioResetSenhaRequest
from src.usecase.usuario.obter_usuario_usecase import ObterUsuarioUsecase
from src.usecase.usuario.processar_usuario_reset_senha_usecase import ProcessarUsuarioResetSenhaUsecase
from src.util.auth import authenticate_user, create_token, decode_refresh_token

router = APIRouter()

@router.post("/forgot-password")
async def forgot_password(request: UsuarioResetSenhaRequest):

    try:

        processar_usuario_reset_senha_usecase = ProcessarUsuarioResetSenhaUsecase()
        processar_usuario_reset_senha_usecase.processar_usuario_reset_senha(request.email)

        return {}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel recuperara a senha do usuario.")

@router.post("/sign-in")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    try:

        usuario = authenticate_user(form_data.username, form_data.password)

        access_token = create_token(usuario, "access", 60)
        refresh_token = create_token(usuario, "refresh", 60*24*3)
        return {
            "user":{
                "id": usuario.id,
                "name": usuario.nome,
                "email": usuario.email,
                "avatar": "images/avatars/brian-hughes.jpg",
                "status": "online"
            },
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=403, detail="Usuário ou senha inválidos")

@router.post("/sign-in-with-token")
async def refresh_access_token(token: dict = Depends(decode_refresh_token)):

    usuario_usecase = ObterUsuarioUsecase()
    usuario = usuario_usecase.obter_por_codigo_usuario(token.get("sub"))

    print(usuario)

    access_token = create_token(usuario, "access", 60)
    refresh_token = create_token(usuario, "refresh", 60*24*3)
    return {
        "user": {
            "id": usuario.codigo_usuario,
            "name": usuario.nome,
            "email": usuario.email,
            "avatar": "images/avatars/brian-hughes.jpg",
            "status": "online"
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }