from sqlalchemy import db


class Ranks:
    id = db.Column('id', Integer,primary_key=True),
    name = db.Column('name', String(10), nullable=False),
