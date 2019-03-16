from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('mysql://root:root@voidlingDatabase/voidling', echo=True)
engine.connect()
metadata = MetaData(bind=engine)


