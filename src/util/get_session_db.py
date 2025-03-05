from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URI


def get_session_db():
    # Create database engine
    engine = create_engine("mysql+pymysql://root:@127.0.0.1/gestaoeventos", echo=False)

    # Create database session
    Session = sessionmaker(engine)
    session = Session()
    return session