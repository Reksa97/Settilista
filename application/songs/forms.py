from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

songkeys = [('Am', 'Am'), ('A', 'A'), ('Bbm', 'Bbm'), ('Bb', 'Bb'), ('Bm', 'Bm'), ('B', 'B'), ('Cm', 'Cm'), ('C', 'C'),
    ('C#m', 'C#m'), ('C#', 'C#'), ('Dm', 'Dm'), ('D', 'D'), ('Ebm', 'Ebm'), ('Eb', 'Eb'), ('Em', 'Em'), ('E', 'E'), ('Fm', 'Fm'), ('F', 'F'), ('F#m', 'F#m'), ('F#', 'F#'),
    ('Gm', 'Gm'), ('G', 'G'), ('G#m', 'G#m'), ('Ab', 'Ab')]

class SongForm(FlaskForm):
    name = StringField("Song name", [validators.Length(min=1,max=63)])
    artist = StringField("Artist name", [validators.Length(min=1,max=63)])
    songkey = SelectField(u'Song key', choices=songkeys)
    length = IntegerField("Song length (seconds)", 
    [validators.NumberRange(min=0, message="Length must be atleast 0")])
    class Meta:
        csrf = False

class SetlistSongForm(FlaskForm):
    setlist = SelectField(u'Setlist', coerce=int)
    songkey = SelectField(u'Song key', choices=songkeys)
    notes = StringField("Notes", [validators.Length(max=255)])
    class Meta:
        csrf = False

class EditSetlistSongForm(FlaskForm):
    name = StringField("Song name", [validators.Length(min=1,max=63)])
    artist = StringField("Artist name", [validators.Length(min=1,max=63)])
    length = IntegerField("Song length (seconds)", 
    [validators.NumberRange(min=0, message="length must be atleast 0")])
    songkey = SelectField(u'Song key', choices=songkeys)
    notes = StringField("Notes", [validators.Length(max=255)])
    class Meta:
        csrf = False
