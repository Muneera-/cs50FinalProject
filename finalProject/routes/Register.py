import sqlite3
import finalProject.server
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from finalProject.helpers import *

register_api = Blueprint('register_api', __name__)

@register_api.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
        # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        conn=finalProject.server.getConnection()
        cursor=conn.cursor()

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        elif not request.form.get("password confirmation"):
            return apology("Passwords must match");
            
        # query database for username
        cursor.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),))
        rows = cursor.fetchall()
    
        # ensure username not in use
        if len(rows) != 0:
            return apology("Username in use")
        
        # query database for email
        cursor.execute("SELECT * FROM users WHERE email = ?", (request.form.get("email"),))
        rows = cursor.fetchall()
    
        # ensure email not in use
        if len(rows) != 0:
            return apology("Email address in use")
        
        
        if request.form.get("password")!=request.form.get("password confirmation"):
            return apology("Passwords must match")

        #encrypt password
        pwd = request.form.get("password");
        encp = pwd_context.encrypt(pwd);

        # save to database
        cursor.execute("INSERT INTO users (username, password, email, name) VALUES(?, ?, ?, ?)", (request.form.get("username"), encp, request.form.get("email"), request.form.get("username")))
        
        cursor.execute("SELECT * FROM users WHERE username=?", (request.form.get("username"),))
        row = cursor.fetchall()
        conn.commit()
        session["user_id"] = row[0][0];
        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

    return apology("You Thought");