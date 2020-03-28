"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from seed import setup_db
from forms import AddPetForm, EditPetForm
from secrets import PET_FINDER_API_KEY, PET_FINDER_SECRET
import requests as HTTP_request
from pet_finder import request_pet_finder_token, get_random_pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

# run seed file with sample data
# setup_db()



@app.route('/')
def list_pets():
    """ Show a list of all pets + PetFinder random pet"""

    pets = Pet.query.all()

    # get random pet from PetFinder API
    pet_finder_pet = get_random_pet()

    return render_template('index.html',
                            pets=pets,
                            pet_name=pet_finder_pet["name"],
                            pet_age=pet_finder_pet["age"],
                            pet_url=pet_finder_pet["photo_url"])


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Form for adding a pet """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data
        flash(f"Added {name} to adoption list.")

        # create a pet instance
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_details(pet_id):
    """ Show a pet's details """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"Pet {pet.name} updated!")
        return redirect('/')

    else:
        return render_template('pet_details.html', pet=pet, form=form)

