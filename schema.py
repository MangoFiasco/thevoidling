from sqlalchemy import *

metadata = MetaData()

ranks = Table('ranks', metadata,
    Column('id', Integer),
    Column('name', String(10), nullable=False),
)

tiers = Table('tiers', metadata,
    Column('id', Integer),
    Column('name', String(3), nullable=False),
)

summoners = Table('summoners', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(32), nullable=False),
    Column('api_id', String(32)),
    Column('rank_id', Integer),
    Column('tier_id',Integer),
    Column('lp',Integer)
)

match_champions = Table('match_summoners',metadata,
    Column('champ_id' Integer),
    Column('is_blue_side',Boolean)
    Column('id',Integer,primary_key=True)
    Column ('match_id',Integer,primary_key=True)
    Column('role_id',Integer)
)

role = Table('role',metadata,
    Column('id',Integer),
    Column('role',String(3))
)
