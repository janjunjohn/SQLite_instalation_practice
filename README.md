# SQLite_installation_practice
practicing SQLite by creating library application

# SQLite Starting Codes
## 1. Operating by SQL Commands
e.g.
```python
import sqlite3

# connect to our database or create a new database
db = sqlite3.connect('books_collection.db')

# create a cursor to control our database
cursor = db.cursor()

# create a new table  with command as SQL(Structured Query Language)
cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY,'
               ' title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)')
               
 # add date to our table and save               
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

```
## 2. Operating by SQLAlchemy
e.g.
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"  # Configure Location and DB Name
db = SQLAlchemy(app)   # Start using SQLAlchemy


# CREATE TABLE MODEL
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # optional: it makes each book object to be identified by its title when printed.
    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()  # CREATE DB

# CREATE RECORD
new_book = Books(id=1, title='Harry Potter', author='J.K.Rowling', rating=9.3)
db.session.add(new_book)
db.session.commit()
```

