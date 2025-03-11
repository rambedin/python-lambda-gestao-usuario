import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URI


def get_session_db():
    # Create database engine

    engine = create_engine("mysql+mysqlconnector://root@localhost:3306/gestaoeventos", echo=False)

    # Create database session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session