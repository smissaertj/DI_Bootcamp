import flask
import flask_migrate
import flask_sqlalchemy

from app.config import Config


def create_app():
	flask_app = flask.Flask(__name__)  # Remember: __name__ is the name of the file where the code is written

	flask_app.config.from_object(Config)

	db = flask_sqlalchemy.SQLAlchemy(flask_app)
	migrate = flask_migrate.Migrate(flask_app, db)

	from app.auth_pb.routes import auth_bp

	flask_app.register_blueprint(auth_bp)

	db.create_all()

	return flask_app
