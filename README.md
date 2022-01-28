# SQLite_instalation_practice
paracticing SQLite by creating libraly application

# SQLite Starting Codes
e.g.
```
import sqlite3

# connect to our database or create a new database
db = sqlite3.connect('books_collection.db')

# create a cursor to control our database
cursor = db.cursor()

# create a new table  with command as SQL(Structured Query Language)
cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY,'
               ' title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, raging FLOAT NOT NULL)')
               
 # add date to our table and save               
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

```
