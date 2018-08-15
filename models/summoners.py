from sqlalchemy import db


class Summoners:
    id = db.Column('id', Integer, primary_key=True),
    name = db.Column('name', String(32), nullable=False),
    api_id = db.Column('api_id', String(32)),
    rank_id = db.Column('rank_id', Integer),
    tier_id = db.Column('tier_id',Integer),
    lp = db.Column('lp',Integer)