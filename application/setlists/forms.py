from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SetlistForm(FlaskForm):
    name = StringField("Setlist name", [validators.Length(min=1,max=144)])

    class Meta:
        csrf = False