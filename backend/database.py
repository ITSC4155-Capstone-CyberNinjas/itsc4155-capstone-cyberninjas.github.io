# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: read string from env variable
engine = create_engine('mysql+mysqlconnector://root:parvardigar1@localhost:3306/CyberNinjas...') 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

