from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song, SetlistSong
from application.songs.forms import SongForm

from application.setlists.models import Setlist
from application.setlists.forms import SetlistForm

@app.route("/setlists/", methods=["GET"])
@login_required
def setlists_index():
    return render_template("setlists/list.html", userSetlists = Setlist.query.filter_by(account_id = current_user.id).all(), otherSetlists = Setlist.query.filter(Setlist.account_id != current_user.id).all())

@app.route("/setlists/new")
@login_required
def setlists_form():
    return render_template("setlists/new.html", form = SetlistForm())

@app.route("/setlists/", methods=["POST"])
@login_required
def setlists_create():
    form = SetlistForm(request.form)

    if not form.validate():
        return render_template("setlists/new.html", form = form)

    s = Setlist(form.name.data)
    s.public = False
    s.account_id = current_user.id
    s.account_username = current_user.username

    db.session().add(s)
    db.session().commit()
    flash("Setlist '" + s.name + "' successfully created!")
    return redirect(url_for("setlists_index"))

@app.route("/setlists/<setlist_id>", methods=["GET"])
@login_required
def setlists_show(setlist_id):

    setlist = Setlist.query.get(setlist_id)

    songs = SetlistSong.query.filter_by(setlist_id = setlist_id).order_by(SetlistSong.notes).all()
    length = 0
    for song in songs:
        length += song.length
    lengthMinutes = length//60
    lengthSeconds = length%60

    return render_template("setlists/show.html", current_user = current_user.id ,songs=songs, setlist=setlist, lengthMinutes=lengthMinutes, lengthSeconds=lengthSeconds)

@app.route("/setlists/<setlist_id>/delete", methods=["POST"])
@login_required
def setlists_delete(setlist_id):
    s = Setlist.query.get(setlist_id)

    if current_user.id != s.account_id :
        flash("You can only delete setlists created by you!")
        return redirect(url_for("setlists_index"))

    db.session().delete(s)
    db.session().commit()
    flash("Setlist '" + s.name + "' successfully deleted!")

    setlistsongs = SetlistSong.query.filter_by(setlist_id = setlist_id).all()

    for setlistsong in setlistsongs:
        db.session().delete(setlistsong)
    db.session().commit()
    flash("Songs in the setlist successfully deleted!")
    return redirect(url_for("setlists_index"))

@app.route("/setlists/<setlist_id>/edit", methods=["GET", "POST"])
@login_required
def setlists_edit(setlist_id):
    s = Setlist.query.get(setlist_id)

    if current_user.id != s.account_id :
        flash("You can only edit setlists created by you!")
        return redirect(url_for("setlists_index"))

    form = SetlistForm(request.form)

    if (request.method == "GET"):
        form.name.default = s.name
        form.process()
        return render_template("setlists/edit.html", form=form, setlist=s)

    if not form.validate():
        return render_template("setlists/edit.html", form=form, setlist=s)
    nimiAluksi = s.name
    s.name = form.name.data
    
    db.session.commit()
    if nimiAluksi != s.name :
        flash("Setlist name successfully changed!")

    return redirect(url_for("setlists_show", setlist_id=s.id))