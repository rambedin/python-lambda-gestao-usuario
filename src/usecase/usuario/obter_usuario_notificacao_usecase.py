from src.adapters.mysql.repositories.usuario_notificacao_repository import UsuarioNotificacaoRepository

class ObterUsuarioNotificacaoUsecase:

    def __init__(self):
        self.repository = UsuarioNotificacaoRepository()

    def obter_por_codigo_dominio_usuario(self, dominio_id: str, id: str):

        ds = self.repository.obter_por_dominio_usuario(dominio_id, id)

        if ds is None:
            raise("Nenhuma notificação encontrada.")

        result = []

        for row in ds.fetchall():

            n = {
                "id": row.id,
                "icon": row.icone,
                "title": row.titulo,
                "description": row.descricao,
                "time": row.data_hora_cadastro,
                "read": "true",
                "useRouter": "false"
            }

            if row.link:
               n["link"] = row.link

            result.append(n)

        return result