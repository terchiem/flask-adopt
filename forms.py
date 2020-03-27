"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, Length


class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Pet Name",
                        validators=[InputRequired()])

    species = StringField("Species",
                        validators=[InputRequired(""),
                        AnyOf(["cat", "dog", "porcupine"])])

    photo_url = StringField("Photo URL",
                        validators=[Optional(), URL()])

    age = StringField("Age",
                        validators=[InputRequired(),
                                    Length(min=0, max=30)])

    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """ Form for editing a pet """

    photo_url = StringField("Photo URL",
                        validators=[Optional(), URL()])
    
    notes = StringField("Notes")

    available = BooleanField("Available")