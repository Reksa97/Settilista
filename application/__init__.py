# flask-sovellus
from flask import Flask
app = Flask(__name__)
import os

# tietokanta
from flask_sqlalchemy import SQLAlchemy

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///songs.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# sovelluksen toiminnallisuudet

from application.songs import models
from application.songs import views

from application.setlists import models
from application.setlists import views

from application.auth import models
from application.auth import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# luodaan taulut tarvittaessa
try:
    db.create_all()
except:
    pass