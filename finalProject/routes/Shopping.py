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
    
    class testCart(object):
	
	    def __init__():
		    total = 0
		    items = {}
	
	    def add_item (item.name, item.quantity, item.price, item.number):
		    total += (quantity * price)
		    items[item_name] = quantity
		
	    def remove_item (item.name, item.quantity, item.price, item.number):
		    total -= (quantity * price)
    		items.pop(item.name, None)
		
	    def checkout (cash_paid):
		    balance = cash_paid - total
		    if balance < 0:
			    print "Cash paid not enough"
		    else:
			    print balance

class Shop (testCart):
	
	def __init__():
		quantity = 100
	
	def remove_item (quantity):
		quantity -= 1
    
    return render_template("shopping.html", testCart=testCart)