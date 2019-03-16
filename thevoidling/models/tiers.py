from sqlalchemy import db

class Tiers:
    id = db.Column('id', Integer,primary_key=True),
    name = db.Column('name', String(3), nullable=False),
