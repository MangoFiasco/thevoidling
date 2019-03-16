from thevoidling import db


class Match(db.model):

    id = db.Column(db.Integer, primary_key=True),
    winner = db.Column(db.Integer),
    avg_mmr = db.Column(db.String(11))
    patch = db.Column(db.Integer)
    game_duration = db.Column(db.Integer)

    match_champions = db.relationship('match_champions',cascade="delete",backref="id")

