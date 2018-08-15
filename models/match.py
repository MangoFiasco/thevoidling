from sqlalchemy import db


class Match(db.model):

    id = db.Column('id',Integer, primary_key=True),
    winner_id = db.Column('winner_id',Integer,ForeignKey('match_champions.id', onDelete=('CASCADE')),nullable=False),
    blue_side_id = db.Column('blue_side_id',Integer,ForeignKey('match_champions.id', onDelete=('CASCADE')),nullable=False)