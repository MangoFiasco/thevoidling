from thevoidling import db


# REPRESENTS I II III IV
class Ranks(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column( db.String(10), nullable=False)
