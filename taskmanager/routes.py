from flask import render_template, current_app
from taskmanager import app, db

@app.route("/")
def home():
    return render_template("base.html")
    