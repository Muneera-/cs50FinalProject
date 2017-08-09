import sqlite3
import finalProject.application
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from finalProject.helpers import *

history_api = Blueprint('history_api', __name__)

@login_api.route("/history", methods=["GET"])
def login():
    """View previous orders"""
        
    conn=finalProject.application.getConnection()
    conn.row_factory = sqlite3.Row
    cursor=conn.cursor()
    
    # get previous orders from database
    cursor.execute("SELECT * FROM orders WHERE userID=?", (session["user_id"],));
    rows = cursor.fetchall();
    
    return render_template("history.html", rows)
