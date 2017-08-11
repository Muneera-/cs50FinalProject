import sqlite3
import finalProject.application
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from finalProject.helpers import *

login_api = Blueprint('login_api', __name__)

@login_api.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        conn=finalProject.application.getConnection()
        conn.row_factory = sqlite3.Row
        cursor=conn.cursor()
        
        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        cursor.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = cursor.fetchall()

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["password"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0][0]

        # redirect user to home page
        return render_template("login.html")

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")