from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

from thevoidling import routes
from thevoidling.models.roles import *

db.create_all()