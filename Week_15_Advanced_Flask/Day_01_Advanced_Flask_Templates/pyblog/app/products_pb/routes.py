import flask
from flask import Blueprint

products_bp = Blueprint('products_pb', __name__, url_prefix='/products_pb', template_folder='templates', static_folder='static')


@products_bp.route('/')
def main():
	return flask.render_template("home.html")
