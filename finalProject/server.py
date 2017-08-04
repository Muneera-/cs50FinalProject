#!/usr/bin/python

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from cartItem import CartItem

from helpers import *

# configure application
app = Flask(__name__)

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

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

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
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[2]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0][0]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    return 0;

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    
        # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        elif not request.form.get("password2"):
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
        
        
        if request.form.get("password")!=request.form.get("password2"):
            return apology("Passwords must match")

        #encrypt password
        pwd = request.form.get("password");
        encp = pwd_context.encrypt(pwd);

        # save to database
        cursor.execute("INSERT INTO users (username, password, email) VALUES(?, ?, ?)", (request.form.get("username"), encp, request.form.get("email"),))
        
        cursor.execute("SELECT * FROM users WHERE username=?", (request.form.get("username"),));
        row = cursor.fetchall();
        
        
        session["user_id"] = row[0][0];

            
        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

    return apology("You Thought");
    
@app.route("/shopping", methods=["GET", "POST"])
def shopping():
    testCart=[]
    for i in range(0,5):
        testCart.append(CartItem(i, i, i))
    return render_template("shopping.html", testCart=testCart)
   


@app.route("/descrip")
def descrip():
    return render_template("descrip.html")


@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/buy", methods=["GET", "POST"])
def buy():
    if(request.method=="POST"):
        #when checkout is clicked
        if request.form["submit"] == "checkout":
            return render_template("shopping.html")
        quantity = int(request.form.get("quantity"))
        itemId = int(request.form.get("itemId"))
        price = cursor.execute("SELECT price FROM inventory WHERE itemID = :itemId", itemId=itemId)
        #create Item to add to cart
        newItem = CartItem(quantity, itemId, price)
        
        #when add item is clicked
        if request.form["submit"] == "addItem":
            #check if item is already in our cart
            isNewItem = True
            for item in shoppingCart:
                if isNewItem is True:
                    if item.itemId == itemId:
                        item.quantity = item.quantity + quantity
                        item.description = cursor.execute("SELECT description FROM inventory WHERE itemID = :itemId", itemId=itemId)
                        item.name = cursor.execute("SELECT name FROM inventory WHERE itemID = :itemId", itemId=itemId)
                        isNewItem = False
            if isNewItem:
                shoppingCart.append(newItem)
        
        #when remove item is clicked
        elif request.form["submit"] == "removeItem":
            if any(item.itemId == itemId for item in shoppingCart):
                #if new quantity is not > 0 remove the item from the cart
                if item.quantity > quantity:
                    item.quantity = item.quantity - quantity
                else:
                    shoppingCart.remove(newItem)
            else:
                return
    return render_template("buy.html")
    

#For when a user forgets their password
@app.route("/forgotten", methods=["GET", "POST"])
def forgot():
    if(request.method=="POST"):
        
        #if no email inputted
        if not(request.form.get("email")):
            return apology("must provide email")
        
        #ensure email exists
        cursor.execute("SELECT * FROM users WHERE email=?", (request.form.get("email"),))
        rows = cursor.fetchall();
        if(len(rows) != 1):
            return apology("email doesn't exist")
            
        
    else:
        return render_template("forgotten.html")