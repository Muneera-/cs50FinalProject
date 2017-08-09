import sqlite3
from passlib.apps import custom_app_context as pwd_context

conn = sqlite3.connect("website.db") # or use :memory: to put it in RAM cursor = conn.cursor()
cursor= conn.cursor()

#Delete all rows in tables
cursor.execute("DELETE FROM users");
cursor.execute("DELETE FROM inventory");
cursor.execute("DELETE FROM mediaType");
cursor.execute("DELETE FROM orders");
cursor.execute("DELETE FROM payment");

#insert test cases
media = ["DVD", "BluRay", "VHS"]
cursor.execute("INSERT INTO mediaType(media) VALUES('DVD')");
cursor.execute("INSERT INTO mediaType(media) VALUES('BluRay')");
cursor.execute("INSERT INTO mediaType(media) VALUES('VHS')");

#Changed to make sure passwords are hashed for each user
cursor.execute("INSERT INTO users(username, password, email) VALUES('a', ?, 'a@aol.com')", (pwd_context.hash("a"),))
cursor.execute("INSERT INTO users(username, password, email) VALUES('b', ?, 'b@aol.com')", (pwd_context.hash("b"),))
cursor.execute("INSERT INTO users(username, password, email) VALUES('c', ?, 'c@aol.com')", (pwd_context.hash("c"),))
cursor.execute("INSERT INTO users(username, password, email) VALUES('d', ?, 'd@aol.com')", (pwd_context.hash("d"),)) 
cursor.execute("INSERT INTO users(username, password, email) VALUES('e', ?, 'e@aol.com')", (pwd_context.hash("e"),))
#conn.commit();

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('5', 'organized crime', '19.00', 'The Godfather', '1', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('4', 'prison escape', '20.00', 'The Shawshank Redemption', '2', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('3', 'upstander in Nazi germany during Holocaust', '21.00', 'Schindlers List', '1', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('2', 'boxer journey', '22.00', 'Raging Bull', '1', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('6', 'expatriate encounters a former lover', '23.00', 'Casablanca', '2', 'romance')")
#conn.commit();

cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('a', '123 Test Street', '1234123412341234', '00/0000', '123', '1')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('b', '124 Test Street', '1234123412341235', '00/0001', '124', '2')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('c', '125 Test Street', '1234123412341236', '00/0002', '125', '3')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('d', '126 Test Street', '1234123412341237', '00/0003', '126', '4')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('e', '127 Test Street', '1234123412341238', '00/0004', '127', '5')")
#conn.commit();

cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('23.45', '1', (SELECT userID FROM users WHERE username='a'), (SELECT itemID FROM inventory WHERE name = 'Raging Bull'), '12345')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('543.67', '2', (SELECT userID FROM users WHERE username = 'b'), (SELECT itemID FROM inventory WHERE name = 'Raging Bull'), '1234')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('4.34', '1', (SELECT userID FROM users WHERE username = 'c'), (SELECT itemID FROM inventory WHERE name = 'Casablanca'), '54321')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('9.00', '2', (SELECT userID FROM users WHERE username = 'd'), (SELECT itemID FROM inventory WHERE name = 'The Shawshank Redemption'), '6780')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('12.00', '2', (SELECT userID FROM users WHERE username = 'e'), (SELECT itemID FROM inventory WHERE name = 'Casablanca'), '5432')")
conn.commit();

#rows = cursor.execute("SELECT * FROM users WHERE username = ?", ('a',))
#pwd_context.verify('a', rows[0]["password"])
#print("Opened database successfully")