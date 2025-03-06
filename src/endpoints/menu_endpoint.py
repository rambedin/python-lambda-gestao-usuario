from fastapi import APIRouter, Depends, HTTPException
from src.util.auth import decode_refresh_token

router = APIRouter()

@router.get("")
async def obter(token: dict = Depends(decode_refresh_token)):

    '''
    dashboard
    eventos
    agenda
    financeiro
    clientes
    fornecedores
    usuarios
    configurações
    '''

    data = [
        {
            "id": "dashboard",
            "title": "Dashboard",
            "type": "basic",
            "icon": "heroicons_outline:cube",
            "link": "/example"
        },
        {
            "id": "eventos",
            "title": "Eventos",
            "type": "basic",
            "icon": "heroicons_outline:cake",
            "link": "/eventos"
        },
        {
            "id": "agenda",
            "title": "Agenda",
            "type": "basic",
            "icon": "heroicons_outline:calendar",
            "link": "/agenda"
        },
        {
            "id": "financeiro",
            "title": "Financeiro",
            "type": "basic",
            "icon": "heroicons_outline:banknotes",
            "link": "/financeiro"
        },
        {
            "id": "clientes",
            "title": "Clientes",
            "type": "basic",
            "icon": "heroicons_outline:user-circle",
            "link": "/clientes"
        },
        {
            "id": "fornecedores",
            "title": "Fornecedores",
            "type": "basic",
            "icon": "heroicons_outline:identification",
            "link": "/fornecedores"
        },
        {
            "id": "usuarios",
            "title": "Usuários",
            "type": "basic",
            "icon": "heroicons_outline:user",
            "link": "/usuarios"
        },
        {
            "id": "config",
            "title": "Configurações",
            "type": "basic",
            "icon": "heroicons_outline:wrench",
            "link": "/config"
        }
    ]

    try:
        return {
            "compact": data,
            "default": data,
            "futuristic": data,
            "horizontal": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Não foi possivel obter as informações de navegação.")