from datetime import datetime, timedelta
from typing import Literal

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


from src.domain.models.usuario import Usuario
from src.usecase.usuario.auth_usuario_usecase import AuthUsuarioUsecase
from src.util.settings import access_token_jwk, refresh_token_jwk

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def authenticate_user(email: str, senha: str) -> Usuario:

    print(f"autenticando o email: {email} e senha: {senha}...")

    auth_usecase = AuthUsuarioUsecase()
    auth = auth_usecase.auth(email, senha)

    if auth is None:
        raise ('Usuario nao encontrado.')

    usuario = Usuario()
    usuario.codigo_usuario = auth.codigo_usuario
    usuario.codigo_dominio = auth.codigo_dominio
    usuario.email = auth.email

    return usuario

def create_token(
    user: Usuario,
    token_type: Literal["refresh", "access"],
    ttl: int
) -> str:
    # This function generates token with any claims you want

    payload = {
        "sub": user.codigo_usuario,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=ttl),
        "email": user.email,
        "tenant": user.codigo_dominio,
        "user_role": user.role
    }

    if token_type == "access":
        key = access_token_jwk
    elif token_type == "refresh":
        key = refresh_token_jwk

    encoded_jwt = jwt.encode(
        payload,
        key,
        "HS256"
    )

    return encoded_jwt

async def decode_access_token(token: str = Depends(oauth2_scheme)) -> dict:
    # This function will be used as dependency in endpoints
    # we want secured. Basically it verifies the JWT and
    # returns its contents as dictionary.

    try:
        payload = jwt.decode(
            token,
            access_token_jwk,
            algorithms="HS256",
        )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {e}"
        )

    return payload

async def decode_refresh_token(token: str = Depends(oauth2_scheme)) -> dict:
    # This function will be used as dependency only
    # when you want to refresh your access token.
    # Since access and refresh tokens have different signing keys,
    # user won't be able to use refresh token to access endpoints
    # protected by access token.

    try:
        payload = jwt.decode(
            token,
            refresh_token_jwk,
            algorithms="HS256",
        )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {e}"
        )

    return payload