import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from finalProject.helpers import *

forgotten_api = Blueprint('forgotten_api', __name__)

#For when a user forgets their password
@forgotten_api.route("/forgotten", methods=["GET", "POST"])
def forgot():
    if(request.method=="POST"):
        
        #if no email inputted
        if not(request.form.get("email")):
            return apology("must provide email")
        
        #ensure email exists
        cursor.execute("SELECT * FROM users WHERE email=?", (request.form.get("email"),))
        rows = cursor.fetchall()
        if(len(rows) != 1):
            return apology("email doesn't exist")
            
        pword = request.form.get("password")
        
        if(request.form.get("password") != request.form.get("password2")):
            return apology("Passwords must match")
            
        if pwd_context.verify(request.form.get("password"), rows[2]):
            return apology("must be new password")
            
        pword = pwd_context.encrypt(pword)
        
        cursor.execute("UPDATE users SET password=? WHERE email=?", (pword, request.form.get("email"),))
    else:
        return render_template("forgotten.html")