from app import db
from datetime import datetime

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    gender = db.Column(db.String(1))
    breed = db.Column(db.String(64))
    date_of_birth = db.Column(db.Date, default=datetime.now().strftime('%Y-%m-%d'))
    price = db.Column(db.Integer)
    image = db.Column(db.String(64))
    cart = db.Column(db.Integer, db.ForeignKey('cart.id'))

    def __repr__(self):
        return f'<Pet: {self.name}>'


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pets = db.relationship('Pet', backref='pet', lazy='dynamic')

    def add_to_cart(self, pet_id):
        pass

    def get_Cart(self):
        pass

    def get_total(self):
        pass