from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SongForm(FlaskForm):
    name = StringField("Song name", [validators.InputRequired()])
    artist = StringField("Artist name", [validators.InputRequired()])
    songkey = StringField("Song key", [validators.InputRequired()])
    length = IntegerField("Song length (seconds)", 
    [validators.NumberRange(min=0, message="length must be atleast 0")])
    class Meta:
        csrf = False