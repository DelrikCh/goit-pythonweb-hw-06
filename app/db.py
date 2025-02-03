from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session, declarative_base


DB_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DB_URL)
session = Session(engine)

Base = declarative_base()
