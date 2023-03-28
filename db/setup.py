from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import settings

db_engine = create_engine(
    settings.db_url, 
    connect_args={
        "check_same_thread": False
})

session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
Base = declarative_base()
