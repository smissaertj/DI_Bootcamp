from app import db

# Many Too Many / Bidirectional Relationship
dogs_table = db.Table('dogs',
                      db.Column('human_id', db.Integer, db.ForeignKey('human.id')),
                      db.Column('dog_id', db.Integer, db.ForeignKey('dog.id'))
)


class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    dogs = db.relationship('Dog', secondary=dogs_table, back_populates="humans")

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    race = db.Column(db.String(64))
    humans = db.relationship('Human', secondary=dogs_table, back_populates="dogs")


""" One To Many 
class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    dogs = db.relationship('Dog', backref='human', lazy='dynamic')
    


class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    race = db.Column(db.String(64))
    master = db.Column(db.Integer, db.ForeignKey('human.id'))
"""


