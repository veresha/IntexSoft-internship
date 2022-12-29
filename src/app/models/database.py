from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
HOST_ADDRESS = os.environ['HOST_ADDRESS']
DB_NAME = os.environ['DB_NAME']
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST_ADDRESS}/{DB_NAME}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
