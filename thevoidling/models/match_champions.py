from thevoidling import db


class MatchChampions(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    account_id = db.Column(db.String(56),db.ForeignKey('summoners.id'),nullable=False)
    champ_id = db.Column(db.Integer),
    match_id = db.Column (db.Integer,db.ForeignKey('match.id'),nullable=False)
    role_id = db.Column(db.Integer)