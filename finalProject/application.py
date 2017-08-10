#!/usr/bin/python

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from finalProject.cartItem import CartItem
from finalProject.helpers import *
from finalProject.routes.Buy import buy_api
from finalProject.routes.Description import description_api
from finalProject.routes.Forgotten import forgotten_api
from finalProject.routes.Login import login_api
from finalProject.routes.Logout import logout_api
from finalProject.routes.Register import register_api
from finalProject.routes.Shopping import shopping_api


# configure application
app = Flask(__name__)

# register routes
app.register_blueprint(buy_api)
app.register_blueprint(description_api)
app.register_blueprint(forgotten_api)
app.register_blueprint(login_api)
app.register_blueprint(logout_api)
app.register_blueprint(register_api)
app.register_blueprint(shopping_api)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#globalVariable for shoppingCart
shoppingCart=[]

# configure use of database
conn = sqlite3.connect("website.db");
cursor = conn.cursor();

def getConnection():
    return conn

@app.route("/")
@login_required
def index():
    return render_template("index.html")