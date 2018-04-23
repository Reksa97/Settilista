from application import db
from application.models import Base

class Song(Base):

    name = db.Column(db.String(144), nullable=False)
    artist = db.Column(db.String(144), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    songkey = db.Column(db.String(144), nullable=False)
    public = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)

    def __init__(self, name):
        self.name = name
        self.public = False

class SetlistSong(Base):

    name = db.Column(db.String(144), nullable=False)
    artist = db.Column(db.String(144), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    songkey = db.Column(db.String(144), nullable=False)
    notes = db.Column(db.String(144), nullable=False)

    setlist_id = db.Column(db.Integer, db.ForeignKey('setlist.id'),
                            nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)

    def __init__(self, name):
        self.name = name
        self.public = False