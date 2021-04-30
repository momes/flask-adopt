"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", 
                        validators=[InputRequired()])

    species = StringField("Species", 
                            validators=[InputRequired()])

    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL()])

    age = RadioField("Age", choices=[('baby', 'Baby'),
                                    ('young', 'Young'),
                                    ('adult', 'Adult'),
                                    ('senior', 'Senior')], 
                            validators=[InputRequired()])

    notes = TextAreaField("Notes")

