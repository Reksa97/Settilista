from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song, SetlistSong
from application.songs.forms import SongForm, SetlistSongForm
from application.auth.models import User
from application.setlists.models import Setlist

@app.route("/", methods=["GET"])
def songs_index():
    return render_template("songs/list.html", songs = Song.query.all(), no_songs=User.find_accounts_with_no_added_songs())

@app.route("/songs/new/")
@login_required
def songs_form():
    return render_template("songs/new.html", form = SongForm())

@app.route("/songs/", methods=["POST"])
def songs_create():
    form = SongForm(request.form)

    if not form.validate():
        return render_template("songs/new.html", form = form)

    s = Song(form.name.data)
    s.artist = form.artist.data
    s.length = form.length.data
    s.songkey = form.songkey.data
    s.account_id = current_user.id

    db.session().add(s)
    
    db.session().commit()

    return redirect(url_for("songs_index"))


@app.route("/songs/<song_id>/", methods=["POST"])
@login_required
def songs_set_public(song_id):

    s = Song.query.get(song_id)

    if s.public == True:
        s.public = False
    else: s.public = True

    db.session().commit()
  
    return redirect(url_for("songs_index"))


@app.route("/songs/<song_id>/tosetlist", methods=["GET", "POST"])
@login_required
def songs_addtosetlist(song_id):

    s = Song.query.get(song_id)
    form = SetlistSongForm(request.form)
    setlists = Setlist.query.filter_by(account_id=current_user.id).all()
    form.setlist.choices = [(setlist.id, setlist.name) for setlist in setlists]
    
    if request.method == "GET":
        return render_template("songs/tosetlist.html", form=form, song=s)
    
    sls = SetlistSong(s.name)
    sls.account_id = current_user.id
    sls.setlist_id = form.setlist.data
    sls.artist = s.artist
    sls.length = s.length
    sls.songkey = form.songkey.data
    
    sls.notes = form.notes.data
    
    db.session().add(sls)
    
    db.session().commit()
    return redirect(url_for("songs_index"))
    

@app.route("/songs/<song_id>/delete", methods=["POST"])
@login_required
def songs_delete(song_id):

    s = Song.query.get(song_id)

    db.session.delete(s)
    db.session.commit()
    flash("Song deleted")

    return redirect(url_for("songs_index"))
