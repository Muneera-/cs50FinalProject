import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from finalProject.cartItem import CartItem

shopping_api = Blueprint('shopping_api', __name__)
# configure use of database

@shopping_api.route("/shopping", methods=["GET", "POST"])
def shopping():
    testCart=[]
    for i in range(0,5):
        testCart.append(CartItem(i, i, i))
    return render_template("shopping.html");