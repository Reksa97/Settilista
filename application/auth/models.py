from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    songs = db.relationship("Song", backref='account', lazy=True)

    def __init__(self, username):
        self.username = username
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_accounts_with_no_added_songs():
        stmt = text("SELECT Account.id, Account.username FROM Account"
                    " LEFT JOIN Song ON Song.account_id = Account.id"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Song.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1]})

        return response