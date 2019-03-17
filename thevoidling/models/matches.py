from thevoidling import db


class Matches(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    riot_match_id = db.Column(db.Integer)
    winner = db.Column(db.Integer)
    avg_mmr = db.Column(db.String(11))
    patch = db.Column(db.Integer)
    game_duration = db.Column(db.Integer)
    champions = db.relationship('MatchChampions',backref='matches', lazy=True)

