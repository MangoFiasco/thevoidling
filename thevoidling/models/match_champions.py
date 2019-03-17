from thevoidling import db
from thevoidling.models.summoners import Summoners

class MatchChampions(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    summoner_id = db.Column(db.Integer,db.ForeignKey('summoners.id'),nullable=False)
    champ_id = db.Column(db.Integer)
    match_id = db.Column (db.Integer,db.ForeignKey('matches.id'),nullable=False)
    role_id = db.Column(db.Integer)