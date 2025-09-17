# Projeto de Autenticação de Usuários - FastAPI + SQLAlchemy + Lambda

Este projeto implementa um serviço de **autenticação de usuários** para login e gestão de credenciais, construído em **Python**, com **FastAPI**, **SQLAlchemy** e preparado para rodar em **AWS Lambda**.  

A arquitetura segue o padrão **Hexagonal (Ports & Adapters)**, separando regras de negócio, camadas de aplicação, adaptação de infraestrutura e endpoints.

---

## Funcionalidades

- Autenticação e login de usuários.  
- Recuperação e redefinição de senha.  
- Perfis e permissões de acesso.  
- Notificação de eventos relacionados ao usuário.  
- Endpoints RESTful documentados automaticamente com **Swagger/OpenAPI**. 

---

## Tecnologias Utilizadas

- **Python 3.10+**  
- **FastAPI** (API REST e documentação automática)  
- **SQLAlchemy** (ORM para persistência de dados)  
- **Uvicorn** (server local para desenvolvimento)  
- **Mangum** (adapter para rodar FastAPI no Lambda)  
- **AWS Lambda & API Gateway**  

---

## Estrutura do Projeto

```
src/
├── adapters/
│ └── mysql/ # Implementações ligadas ao banco de dados
│ ├── models/
│ └── repositories/
│
├── domain/ # Regras de negócio e entidades
│ ├── exceptions/ # Exceções de domínio
│ └── models/ # Modelos de domínio (Usuario, Perfil, etc.)
│
├── endpoints/ # Interfaces HTTP (FastAPI)
│ ├── requests/ # Schemas de entrada
│ ├── responses/ # Schemas de saída
│ ├── auth_endpoint.py # Endpoints de autenticação/login
│ ├── menu_endpoint.py
│ ├── navegacao_item_endpoint.py
│ ├── notificacao_endpoint.py
│ └── usuario_endpoint.py
│
├── usecase/ # Casos de uso (lógica de aplicação)
│ └── usuario/
│ ├── auth_usuario_usecase.py
│ ├── obter_usuario_usecase.py
│ ├── processar_usuario_reset_senha_usecase.py
│ └── ...
│
├── util/ # Utilitários e helpers
│ ├── auth.py
│ ├── base_declarative.py
│ ├── get_session_db.py
│ ├── logger.py
│ ├── settings.py
│ └── debugger.py
│
├── config.py # Configurações globais
└── main.py # Ponto de entrada da aplicação
```

---

## Pré-requisitos

- Python 3.10+  
- MySQL rodando (ou outro banco compatível com SQLAlchemy)  
- Conta AWS para deploy serverless  

---

## Como rodar localmente

1. Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente do banco de dados, por exemplo:

```bash
DATABASE_USERNAME
DATABASE_PASSWORD 
DATABASE_HOST 
DATABASE_PORT
DATABASE_NAME 
```

3. Execute o servidor local:

```bash
uvicorn main:app --reload
```

4. Acesse a documentação interativa em:

- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)