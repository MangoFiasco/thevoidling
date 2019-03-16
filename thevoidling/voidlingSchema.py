from thevoidling import db


class Summoner(db.Model):
    id
    name
    rank
    
class Mastery(db.Model):
    id
    summoner_id
    champ_id
    points
    level

class Match(db.Model):
    id
    winner
    avg_mmr
    patch
    gameduration

class MatchUp(db.Model):
    champ_id
    team
    Lane
    summoner_id
    match_id

class 
