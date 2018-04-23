from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song, SetlistSong
from application.songs.forms import SongForm

from application.setlists.models import Setlist
from application.setlists.forms import SetlistForm

@app.route("/setlists/", methods=["GET"])
def setlists_index():
    return render_template("setlists/list.html", setlists = Setlist.query.all())

@app.route("/setlists/new")
@login_required
def setlists_form():
    return render_template("setlists/new.html", form = SetlistForm())

@app.route("/setlists/", methods=["POST"])
def setlists_create():
    form = SetlistForm(request.form)

    if not form.validate():
        return render_template("setlists/new.html", form = form)

    s = Setlist(form.name.data)
    s.length = 0
    s.public = False
    s.account_id = current_user.id

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("setlists_index"))

@app.route("/setlists/<setlist_id>", methods=["GET"])
def setlists_show(setlist_id):

    setlist = Setlist.query.get(setlist_id)

    songs = SetlistSong.query.filter_by(setlist_id = setlist_id).all()

    return render_template("setlists/show.html", songs=songs, setlist=setlist)