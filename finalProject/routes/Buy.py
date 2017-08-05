import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from finalProject.cartItem import CartItem
from finalProject.helpers import *

buy_api = Blueprint('buy_api', __name__)

@buy_api.route("/buy", methods=["GET", "POST"])
@login_required
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