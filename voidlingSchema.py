from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('mysql://root:root@voidlingDatabase/voidling', echo=True)
engine.connect()
metadata = MetaData(bind=engine)

class Ranks:
    id = db.Column('id', Integer,primary_key=True),
    name = db.Column('name', String(10), nullable=False),


class Tiers:
    id = db.Column('id', Integer,primary_key=True),
    name = db.Column('name', String(3), nullable=False),


class Summoners:
    id = db.Column('id', Integer, primary_key=True),
    name = db.Column('name', String(32), nullable=False),
    api_id = db.Column('api_id', String(32)),
    rank_id = db.Column('rank_id', Integer),
    tier_id = db.Column('tier_id',Integer),
    lp = db.Column('lp',Integer)

class Match_champions:
    id = db.Column('id',Integer,primary_key=True)
    champ_id = db.Column('champ_id' Integer),
    match_id = db.Column ('match_id',Integer,ForeignKey('match.id', onDelete=('CASCADE')),nullable=False)
    role_id = db.Column('role_id',Integer)
    
class Rolse:
    id = db.Column('id',Integer,primary_key=True),
    role = db.Column('role',String(3))


print("DATABASE CREATED")