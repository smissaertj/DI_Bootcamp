import flask
from app import app, db
from app.models import Human, Dog


@app.route('/')
def index():
    bob = Human(name='Bob')
    alice = Human(name='Alice')
    rex = Dog(name='Rex', race='Malinois', humans=[bob, alice])
    scooby = Dog(name='Scooby', race='Doo', humans=[bob])

    db.session.add_all([bob, alice, rex, scooby])
    db.session.commit()
    return 'Done'

@app.route('/get_dogs/<human_id>')
def get_dogs(human_id):

    human = Human.query.filter_by(id=human_id).first()
    return flask.render_template('get_dogs.html', dogs=human.dogs)