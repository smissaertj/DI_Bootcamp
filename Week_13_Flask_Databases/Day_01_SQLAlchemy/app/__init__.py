import flask
import os

import flask_migrate
import flask_sqlalchemy

flask_app = flask.Flask(__name__)
flask_app.config['SECRET_KEY'] = 'de23f8ff85ffbf5518837a9a17ca0fe1028d8bda0306dafc'

basedir = os.path.abspath(os.path.dirname(__file__))  # Try to avoid hardcoding paths, use os
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import routes, models
