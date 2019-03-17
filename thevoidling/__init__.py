import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
user = os.environ['DB_USER']
password = os.environ['DB_PASS']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{user}:{password}@{host}:{port}/{db_name}"

db = SQLAlchemy(app)

# from thevoidling import routes
from thevoidling.models.roles import *

# db.create_all()
print(db.session.query(Roles)[0].id)
