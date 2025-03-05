import json
import platform
from venv import logger

from fastapi import FastAPI
from mangum import Mangum
from starlette.config import environ

from src.endpoints.usuario_endpoint import router as usuario_router, login_for_access_token

app = FastAPI()

#inclui os endpoints routers
app.include_router(usuario_router, prefix="/usuario", tags=["usuario"])

handler = Mangum(app)

#handler do lambda
def lambda_handler(event, context):
    logger.info("handler iniciado...")
    return handler(event, context)

#main local
def main(event=None):
    if platform.system() == 'Linux':
        globals()['__TMP_PATH__'] = '/tmp/'
    if platform.system() == 'Windows':
        globals()['__TMP_PATH__'] = './tmp/'
    if not event:
        with open('request.json', 'r') as f:
            event = json.loads(f.read())
    print(lambda_handler(event, None))

#main
if __name__ == '__main__':

    print("gerando um token valido com jose:")

    #verifica se esta sendo executando localmente.
    if environ.get('LOCAL') is not None:
        logger.info("executando local...")
        main()