from thevoidling import db


# REPRESENTS GOLD SILVER BRONZE IRON ETC
class Tiers(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(11), nullable=False)
