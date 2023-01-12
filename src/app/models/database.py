from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.app.config import DB_USER, DB_PASSWORD, HOST_ADDRESS

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST_ADDRESS}/postgres'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
