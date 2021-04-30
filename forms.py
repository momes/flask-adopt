"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet Name", 
        validators=[InputRequired()]
    )

    species = RadioField(
        "Species", 
        choices=[
            ('cat', 'Cat'),
            ('dog', 'Dog'),
            ('porcupine', 'Porcupine')],
        validators=[InputRequired()]
    )

    photo_url = StringField(
        "Photo URL", 
        validators=[
            Optional(), 
            URL()]
        )

    age = RadioField(
        "Age", 
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')], 
            validators=[InputRequired()])

    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing pet profile."""

    photo_url = StringField(
        "Photo URL", 
        validators=[
            Optional(), 
            URL()]
        )

    notes = TextAreaField("Notes")

    available = BooleanField(
        "Available",
        validators=[Optional()]
    )

