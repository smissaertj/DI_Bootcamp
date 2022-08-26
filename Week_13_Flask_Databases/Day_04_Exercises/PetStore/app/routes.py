from app import app, db, models
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('pets'))

@app.route('/pets')
def pets():
    all_pets = models.Pet.query.all()
    return render_template('pets.html', pets=all_pets)

@app.route('/pet/<int:pet_id>')
def pet(pet_id):
    pet = models.Pet.query.filter_by(id=pet_id).first()
    return render_template('pet.html', pet_details=pet)

@app.route('/add_pet/<int:pet_id>')
def add_to_cart(pet_id):
    pet = models.Pet.query.filter_by(id=pet_id).first()
    return redirect(url_for('pets'))

@app.route('/cart')
def cart():
    return render_template('cart.html')