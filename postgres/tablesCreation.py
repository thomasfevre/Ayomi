from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin


#####   POSTGRES TABLES INIT    ######


base = declarative_base()

class Accounts(base, UserMixin):
    __tablename__ = "accounts"

    id = Column('id', Integer, primary_key=True)
    email = Column('email', String, unique=True)
    password = Column('password', String, unique=True)    


engine = create_engine('postgresql://ayomi:admin@localhost:5432/ayomi', echo=False, pool_size=20, max_overflow=30)
base.metadata.create_all(bind=engine)


