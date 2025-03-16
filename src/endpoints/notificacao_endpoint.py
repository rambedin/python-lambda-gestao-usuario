from fastapi import APIRouter, Depends, HTTPException

from src.endpoints.requests.notificacao_request import NotificacaoRequest
from src.endpoints.responses.notificacao_response import NotificacaoResponse
from src.usecase.usuario.usuario_notificacao_usecase import UsuarioNotificacaoUsecase
from src.usecase.usuario.obter_usuario_notificacao_usecase import ObterUsuarioNotificacaoUsecase
from src.util.auth import decode_refresh_token
from src.util.logger import logger

router = APIRouter()

@router.get("")
async def obter(token: dict = Depends(decode_refresh_token)):
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
        logger.error(f"Não foi possivel obter as notificações do usuário: {e}")
        raise HTTPException(status_code=500, detail="Não foi possivel obter as notificações do usuário.")

@router.patch("")
async def atualizar(request: NotificacaoRequest, token: dict = Depends(decode_refresh_token)):
    try:

        print(request)

        usecase = UsuarioNotificacaoUsecase()
        notificacao_atualizada = usecase.atualizar_notificacao_lida(request.id)

        return NotificacaoResponse(
            id=notificacao_atualizada.id,
            icon=notificacao_atualizada.icone,
            title=notificacao_atualizada.titulo,
            description=notificacao_atualizada.descricao,
            time=notificacao_atualizada.data_hora_cadastro,
            read=notificacao_atualizada.lida,
            link=notificacao_atualizada.link,
            useRouter=notificacao_atualizada.e_rota
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel atualizar a notificação do usuário.")

@router.delete("")
async def excluir(id: str, token: dict = Depends(decode_refresh_token)):
    try:

        logger.info(id)

        usecase = UsuarioNotificacaoUsecase()
        usecase.excluir_notificacao(id)

        return True

    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel excluir a notificação do usuário.")