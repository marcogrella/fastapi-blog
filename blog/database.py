from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import models
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session


# conexão com a base de dados, além de conectar, cria as tabelas.

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/blogfastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency, é adicionado para criar uma sessão no bd. Toda a vez que uma requisição é chamada
# utiliza-se esse método abaixo.


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# esse é importante, vem da própria documentação que faz o binding entre as tabelas e a conexão (cria tabelas)
Base.metadata.create_all(bind=engine)


while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database='blogfastapi', user='postgres',
        password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection wass sucessfull!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)