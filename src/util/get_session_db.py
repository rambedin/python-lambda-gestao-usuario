from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

# 🔹 Criando o engine do banco de dados
engine = create_engine("mysql+mysqlconnector://root@localhost:3306/gestaoeventos", echo=False, pool_pre_ping=True)

# 🔹 Criando a fábrica de sessões
SessionFactory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(SessionFactory)  # Gerencia sessões automaticamente

# 🔹 Função para obter uma sessão manualmente (caso necessário)
def get_session_db():
    return Session()

# 🔹 Gerenciador de sessão para uso seguro com `with`
@contextmanager
def session_scope():
    session = Session()
    try:
        yield session  # Retorna a sessão ativa para uso no bloco `with`
        session.commit()  # Confirma a transação ao final do bloco
    except Exception as e:
        session.rollback()  # Em caso de erro, desfaz a transação
        raise e
    finally:
        session.close()  # Fecha a sessão corretamente
