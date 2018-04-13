from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class SongForm(FlaskForm):
    name = StringField("Song name", [validators.required()])
    artist = StringField("Artist name", [validators.required()])
    songkey = SelectField(u'Song key', choices=[('Am', 'Am'), ('A', 'A'), ('Bbm', 'Bbm'), ('Bb', 'Bb'), ('Bm', 'Bm'), ('B', 'B'), ('Cm', 'Cm'), ('C', 'C'),
    ('C#m', 'C#m'), ('C#', 'C#'), ('Dm', 'Dm'), ('D', 'D'), ('Ebm', 'Ebm'), ('Eb', 'Eb'), ('Em', 'Em'), ('E', 'E'), ('Fm', 'Fm'), ('F', 'F'), ('F#m', 'F#m'), ('F#', 'F#'),
    ('Gm', 'Gm'), ('G', 'G'), ('G#m', 'G#m'), ('Ab', 'Ab')])
    length = IntegerField("Song length (seconds)", 
    [validators.NumberRange(min=0, message="length must be atleast 0")])
    class Meta:
        csrf = False

class SetlistSongForm(FlaskForm):
    setlist_id = SelectField(u'Setlist', coerce=int)
    songkey = SelectField(u'Song key', choices=[('Am', 'Am'), ('A', 'A'), ('Bbm', 'Bbm'), ('Bb', 'Bb'), ('Bm', 'Bm'), ('B', 'B'), ('Cm', 'Cm'), ('C', 'C'),
    ('C#m', 'C#m'), ('C#', 'C#'), ('Dm', 'Dm'), ('D', 'D'), ('Ebm', 'Ebm'), ('Eb', 'Eb'), ('Em', 'Em'), ('E', 'E'), ('Fm', 'Fm'), ('F', 'F'), ('F#m', 'F#m'), ('F#', 'F#'),
    ('Gm', 'Gm'), ('G', 'G'), ('G#m', 'G#m'), ('Ab', 'Ab')])
    notes = StringField("Notes", [validators.InputRequired])