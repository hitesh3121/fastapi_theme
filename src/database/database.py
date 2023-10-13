import os
# from dotenv import load_dotenv
# from pathlib import Path
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base

# env_path = Path('.')/'.env'
# load_dotenv(dotenv_path=env_path)


# class Development_Settings:
#     POSTGRES_USER: str = os.getenv("POSTGRES_USER")
#     POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
#     POSTGRES_SERVER = os.getenv('POSTGRES_SERVER')
#     POSTGRES_PORT = os.getenv('POSTGRES_PORT')
#     POSTGRES_DB = os.getenv('POSTGRES_DB')
#     DATABASE_URL = os.getenv('DATABASE_URL')
    
#     # POSTGRES_USER: str = "postgres"
#     # POSTGRES_PASSWORD = "mihir"
#     # POSTGRES_SERVER = "localhost"
#     # POSTGRES_PORT = 5432
#     # POSTGRES_DB = "Todo"
#     # DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


# # s//{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# settings = Development_Settings()


SQLALCHEMY_DATABASE_URL = "postgresql://postgres_test:En0G67p4jzyQxGtYeMqYA8n7Qedtgv5d@dpg-ckke84bj89us73au19k0-a.oregon-postgres.render.com/fastapi_pg"


engine = create_engine(SQLALCHEMY_DATABASE_URL, client_encoding='utf8')

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
