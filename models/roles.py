from sqlalchemy import db
    
class Rolse:
    id = db.Column('id',Integer,primary_key=True),
    role = db.Column('role',String(3))
