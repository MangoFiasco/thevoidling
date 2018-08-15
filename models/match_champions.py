from sqlalchemy import db


class MatchChampions:
    id = db.Column('id',Integer,primary_key=True)
    champ_id = db.Column('champ_id' Integer),
    match_id = db.Column ('match_id',Integer,ForeignKey('match.id', onDelete=('CASCADE')),nullable=False)
    role_id = db.Column('role_id',Integer)