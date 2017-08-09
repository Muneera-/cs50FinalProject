import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

logout_api = Blueprint('logout_api', __name__)
# configure use of database
conn = sqlite3.connect("website.db");
cursor = conn.cursor();

@logout_api.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login_api.login"))