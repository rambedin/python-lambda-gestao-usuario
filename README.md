# 🌀 Lambda FastAPI - Gestão de Usuários

Este projeto implementa uma **AWS Lambda** em **Python** para **gestão de usuários**, construída sobre **FastAPI** e **SQLAlchemy**, utilizando a **Arquitetura Hexagonal (Ports & Adapters)**.  

A organização do código foi estruturada em camadas (`domain`, `usecase`, `adapters`, `endpoint`) para garantir **separação de responsabilidades**, **facilidade de testes** e **alta manutenibilidade**.

---

## 🚀 Funcionalidades

- CRUD completo de usuários (criar, listar, atualizar, excluir).  
- Endpoints documentados automaticamente via **Swagger/OpenAPI**.  
- Integração com banco de dados via **SQLAlchemy ORM**.  
- Deploy serverless em **AWS Lambda + API Gateway**.  
- Estrutura hexagonal garantindo baixo acoplamento entre camadas.  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**  
- **FastAPI** (API REST e documentação automática)  
- **SQLAlchemy** (ORM para persistência de dados)  
- **Uvicorn** (server local para desenvolvimento)  
- **Mangum** (adapter para rodar FastAPI no Lambda)  
- **AWS Lambda & API Gateway**  

---

## 📂 Estrutura do Projeto

```
.
├── domain/                 # Regras de negócio e entidades do domínio
│   └── user.py             # Entidade User
│
├── usecase/                # Casos de uso (regras de aplicação)
│   └── user_usecase.py     # Lógica de criação, listagem, atualização e exclusão
│
├── adapters/               # Portas de entrada/saída (banco, repositórios)
│   ├── database.py         # Configuração do SQLAlchemy
│   └── user_repository.py  # Implementação do repositório de usuários
│
├── endpoint/               # Interface HTTP (FastAPI)
│   └── user_endpoint.py    # Rotas e controladores de usuário
│
├── main.py                 # Ponto de entrada (FastAPI + Mangum)
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação
```

---

## 📋 Pré-requisitos

- **Python 3.10+**  
- Conta AWS configurada (para deploy com Lambda + API Gateway)  
- Banco de dados relacional (ex: PostgreSQL, MySQL ou SQLite local para testes)  

---

## ⚡ Como rodar localmente

1. Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente do banco de dados, por exemplo:

```bash
export DATABASE_URL="sqlite:///./users.db"
```

3. Execute o servidor local:

```bash
uvicorn main:app --reload
```

4. Acesse a documentação interativa em:

- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## ☁️ Deploy na AWS Lambda

Este projeto utiliza **Mangum** para rodar o FastAPI em Lambda.  
O `main.py` expõe o handler compatível com o Lambda:

```python
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# importa e inclui os endpoints
from endpoint import user_endpoint
app.include_router(user_endpoint.router)

handler = Mangum(app)
```

Para deploy:

1. Empacote o projeto em `.zip` (com dependências).  
2. Suba no **AWS Lambda** (runtime: Python 3.10).  
3. Configure o **API Gateway** para expor os endpoints REST.  

---

## 📑 Exemplo de Endpoint

### Criar usuário
```http
POST /users
Content-Type: application/json

{
  "name": "Ramon Bedin",
  "email": "ramon@example.com"
}
```

### Resposta
```json
{
  "id": 1,
  "name": "Ramon Bedin",
  "email": "ramon@example.com"
}
```

---

## 📜 Licença

Este projeto é livre para estudos e melhorias. 🚀
