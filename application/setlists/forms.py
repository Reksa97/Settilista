from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SetlistForm(FlaskForm):
    name = StringField("Setlist name", [validators.required()])

    class Meta:
        csrf = False