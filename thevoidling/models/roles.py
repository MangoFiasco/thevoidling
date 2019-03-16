from thevoidling import db
    
class Roles(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.String(10))
