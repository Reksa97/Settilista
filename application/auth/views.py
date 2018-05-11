from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm
from application.songs.models import Song
from application.setlists.models import Setlist

@app.route("/", methods=["GET"])
def frontpage():
    users = User.query.count()
    songs = Song.query.count()
    setlists = Setlist.query.count()
    return render_template("auth/frontpage.html", users=users, songs=songs, setlists=setlists, current_user=current_user)

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("frontpage"))    

@app.route("/auth/logout", methods = ["GET", "POST"])
def auth_logout():
    logout_user()
    return redirect(url_for("frontpage"))

@app.route("/auth/signup", methods = ["GET"])
def auth_signup():
    return render_template("auth/signupform.html", form = SignupForm())

@app.route("/auth/signup/new", methods = ["POST"])
def auth_signup_new():
    form = SignupForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/signupform.html", form = form,
                    error = "User with that username already exists")

   
    if not form.validate() or form.username.data.isspace():
        # username can't be only space
        if form.username.data.isspace():
            form.username.errors.append("Username can't be only whitespace")
        return render_template("auth/signupform.html", form = form)

    

    u = User(form.username.data)
    u.name = form.name.data
    u.password = form.password.data

    db.session().add(u)
    db.session().commit()

    flash("Account successfully created")
    return redirect(url_for("auth_login"))
