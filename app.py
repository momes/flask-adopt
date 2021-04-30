"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash, request

from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data

        notes = form.notes.data
        notes = notes if notes else None

        photo_url = form.photo_url.data
        photo_url = photo_url if photo_url else None

        pet = Pet(name=name, 
                species=species, 
                age=age, 
                notes=notes,
                photo_url=photo_url)

        db.session.add(pet)
        db.session.commit()

        return redirect('/add')        

    else:
        return render_template('add_pet_form.html', form=form)
