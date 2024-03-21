from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from decouple import config

URL_DB = config('URL_DB')

engine = create_engine(url=URL_DB, pool_pre_ping=True)

Session = sessionmaker()