import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

description_api = Blueprint('description_api', __name__)

@description_api.route("/descrip")
def descrip():
    return render_template("descrip.html")