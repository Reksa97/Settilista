from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song, SetlistSong
from application.songs.forms import SongForm, SetlistSongForm, EditSetlistSongForm
from application.auth.models import User
from application.setlists.models import Setlist

@app.route("/", methods=["GET"])
@login_required
def songs_index():
    return render_template("songs/list.html", songs = Song.query.filter((Song.public==True) | (Song.account_id == current_user.id))
                                .order_by(Song.account_id != current_user.id).all(), no_songs=User.find_accounts_with_no_added_songs(), current_user_id=current_user.id)

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

    flash("Song successfully created!")
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

@app.route("/songs/<song_id>/edit", methods=["GET","POST"])
@login_required
def songs_edit(song_id):

    s = Song.query.get(song_id)

    if s.account_id != current_user.id:
        flash("You can only edit songs you've added yourself!")
        return redirect(url_for("songs_index"))

    form = SongForm(request.form)

    if request.method == "GET":
        form.name.default = s.name
        form.artist.default = s.artist
        form.length.default = s.length
        form.songkey.default = s.songkey
        form.process()
        return render_template("songs/edit.html", form=form, song=s)



    s.name = form.name.data
    s.artist = form.artist.data
    s.length = form.length.data
    s.songkey = form.songkey.data

    db.session().commit()
    flash("Song successfully edited!")
    return redirect(url_for("songs_index"))


@app.route("/songs/<song_id>/tosetlist", methods=["GET", "POST"])
@login_required
def songs_addtosetlist(song_id):

    s = Song.query.get(song_id)
    form = SetlistSongForm(request.form)
    setlists = Setlist.query.filter_by(account_id=current_user.id).all()
    form.setlist.choices = [(setlist.id, setlist.name) for setlist in setlists]
    
    if request.method == "GET":
        form.songkey.default = s.songkey
        form.process()
        return render_template("songs/tosetlist.html", form=form, song=s)
    
    if not form.validate():
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
    flash("Song successfully added to the setlist")
    return redirect(url_for("setlists_show", setlist_id=sls.setlist_id))
    

@app.route("/songs/<song_id>/delete", methods=["POST"])
@login_required
def songs_delete(song_id):

    s = Song.query.get(song_id)

    if song.account_id != current_user.id:
        flash("You can only delete songs you've added yourself!")
        return redirect(url_for("songs_index"))

    db.session.delete(s)
    db.session.commit()
    flash("Song deleted")

    return redirect(url_for("songs_index"))

@app.route("/setlistsongs/<setlistsong_id>/edit", methods=["GET", "POST"])
@login_required
def setlistsongs_edit(setlistsong_id):

    s = SetlistSong.query.get(setlistsong_id)

    if s.account_id != current_user.id:
        flash("You can only edit songs in your own setlists!")
        return redirect(url_for("songs_index"))

    form = EditSetlistSongForm(request.form)

    if (request.method == "GET"):
        form.name.default = s.name
        form.artist.default = s.artist
        form.length.default = s.length
        form.songkey.default = s.songkey
        form.notes.default = s.notes
        form.process()
        return render_template("songs/editsetlistsong.html", form=form, setlistsong=s)

    if not form.validate():
        return render_template("songs/editsetlistsong.html", form=form, setlistsong=s)

    s.name = form.name.data
    s.artist = form.artist.data
    s.length = form.length.data
    s.songkey = form.songkey.data
    s.notes = form.notes.data
    
    db.session.commit()

    return redirect(url_for("setlists_show", setlist_id=s.setlist_id))

@app.route("/setlistsongs/<setlistsong_id>/delete", methods=["POST"])
@login_required
def setlistsongs_delete(setlistsong_id):

    s = SetlistSong.query.get(setlistsong_id)

    if s.account_id != current_user.id :
        flash("You can delete songs only from a setlist you've created!")
        return redirect(url_for("setlists_index"))

    db.session.delete(s)
    db.session.commit()
    flash("Song deleted")

    return redirect(url_for("setlists_show", setlist_id=s.setlist_id))