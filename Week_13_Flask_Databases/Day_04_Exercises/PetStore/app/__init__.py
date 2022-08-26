from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Flask Object
app = Flask(__name__)
#  print(os.urandom(56).hex())
app.config['SECRET_KEY'] = '8621a178fa36f43ad89fd885015b7b46eb0a98708c94a3d598124d40e0a60b382bcef7b60e5a917818bb5674fadb3041060bbfe5e42dcc86'

# Database Config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes