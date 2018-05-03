from application import db
from application.models import Base

class Setlist(Base):

    name = db.Column(db.String(144), nullable=False)
    public = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)
    account_username = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        self.public = False