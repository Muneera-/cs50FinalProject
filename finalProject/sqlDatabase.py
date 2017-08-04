import sqlite3
conn = sqlite3.connect("website.db")
cursor= conn.cursor()

#delete preexisting tables
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS inventory")
cursor.execute("DROP TABLE IF EXISTS mediaType")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS payment")

#create tables
cursor.execute("""CREATE TABLE users(
                  userID INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT,
                  password TEXT,
                  email TEXT,
                  name TEXT, 
                  active INTEGER DEFAULT 1)
               """)
               
cursor.execute("""CREATE TABLE payment(
                  ccID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  ccName TEXT, 
                  address TEXT, 
                  ccNumber INTEGER,
                  exp TEXT, 
                  ccv integer, 
                  userID integer, 
                  FOREIGN KEY(userID) REFERENCES users(userID))
               """)               

#created to prevent invalid media types
cursor.execute("""CREATE TABLE mediaType(
                  mediaID INTEGER PRIMARY KEY AUTOINCREMENT, 
                  media TEXT NOT NULL UNIQUE)
               """)
               
cursor.execute("""CREATE TABLE inventory(
                  itemID INTEGER PRIMARY KEY AUTOINCREMENT,
                  apiID INTEGER UNIQUE,
                  quantity INTEGER NOT NULL,
                  description TEXT,
                  price NUMERIC NOT NULL DEFAULT '0.0',
                  name TEXT NOT NULL,
                  mediaID INTEGER,
                  img_url TEXT,
                  genre TEXT NOT NULL DEFAULT '0',
                  FOREIGN KEY (mediaID) REFERENCES mediaType(mediaID))
               """)
               
cursor.execute("""CREATE TABLE orders(
                  orderNum INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  ccID INTEGER NOT NULL,
                  total NUMERIC NOT NULL,
                  itemID INTEGER NOT NULL, 
                  userID INTEGER NOT NULL,
                  quantity INTEGER NOT NULL,
                  time TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY (itemID) REFERENCES inventory(itemID),
                  FOREIGN KEY (ccID) REFERENCES payment(ccID),
                  FOREIGN KEY (userID) REFERENCES users(userID))
               """)
 
# commit the changes
conn.commit()
# close the database connection
conn.close()


#idea for later              
#cursor.execute("CREATE TRIGGER invalidAmount BEFORE UPDATE on inventory WHEN old.quantity<0")
               
print("Opened database successfully")