from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



#  CREATE DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_rating_library.db'  # [<local_file>://<host>/<path>] のhostを省略した結果三重スラッシュになる
db = SQLAlchemy(app)


#  CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# CREATE DB FILE
db.create_all()


@app.route('/')
def home():
    #  READE ALL RECORDS
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)



@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        #  CREATE A RECORD
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # UPDATE A RECORD
        book_id = request.args.get('id')
        book_to_edit = Book.query.get(book_id)
        book_to_edit.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', book=book_selected)


@app.route('/delete')
def delete():
    # DELETE A RECORD BY ID
    book_id = request.args.get('id')
    book_to_edit = Book.query.get(book_id)
    db.session.delete(book_to_edit)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

