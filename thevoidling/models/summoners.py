from thevoidling import db


class Summoners(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(32), nullable=False),
    api_id = db.Column(db.String(32)),
    rank_id = db.Column(db.Integer),
    tier_id = db.Column(db.Integer),
    lp = db.Column(db.Integer)

    match_champions = db.relationship('match_champions',cascade="delete",backref="id")
