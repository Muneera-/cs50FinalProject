import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from finalProject.helpers import *

index_api = Blueprint('index_api', __name__)

@index_api.route("/")
def index():
    return render_template("index.html")