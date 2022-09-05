import flask
from flask import Blueprint

auth_bp = Blueprint('authentication', __name__, url_prefix='/auth_pb', template_folder='templates', static_folder='static')


@auth_bp.route('/login')
def index():
	return flask.render_template("index.html")


@auth_bp.route('/')
def main():
	return flask.render_template("home.html")
