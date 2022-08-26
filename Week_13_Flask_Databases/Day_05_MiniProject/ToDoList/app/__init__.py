from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Flask Object
app = Flask(__name__)
#  print(os.urandom(56).hex())
app.config['SECRET_KEY'] = 'cc36274288c78b86dbda92926786ca8d9bd38dbd9d3c7bcd8545c220df458b4139af91a0584a9c32b8e194469d162470d3b2f99e56d38203'

# Database Config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes