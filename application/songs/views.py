from application import app, db
from flask import render_template, request
from application.songs.models import Song

@app.route("/songs/new/")
def songs_form():
    return render_template("songs/new.html")

@app.route("/songs/", methods=["POST"])
def songs_create():
    print(request.form.get("name"))
  
    return "hello world!"