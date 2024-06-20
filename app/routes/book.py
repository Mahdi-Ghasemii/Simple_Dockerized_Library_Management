from flask import Blueprint , render_template , request , redirect , url_for
from models.model import *

book_app = Blueprint('book', __name__, template_folder='templates')

@book_app.route('/books')
def list_books_route():
      books = select_all_books()
      return render_template("books.html" , books=books)

@book_app.route('/add_book' , methods={"GET" , "POST"})
def add_book_route():
    if request.method == "POST":
      form = BookForm(request.form)
      try: 
        insert_book(form.title.data,form.numPages.data,form.author.data)
        return redirect(url_for("book.list_books_route"))
      except Exception as e:
         return render_template("add_book.html" , form=form , error="Error : " + str(e)) , 400
    elif request.method == "GET":
      form = BookForm()
      return render_template("add_book.html" , form=form)
    

@book_app.route('/delete_book/' , methods={"POST"})
def delete_book_route():
    id = request.args.get('id')
    delete_book(id)
    return redirect(url_for("list_books_route"))


@book_app.route('/edit_book/<id>' , methods={"GET" , "POST"})
def edit_book_route(id):
    cursor = mysql.connection.cursor()
    [bookform , book] = select_book_using_id(id)
    print(book)
    if request.method == "POST":
      form = BookForm(request.form)
      try: 
        update_book(form.title.data,form.numPages.data,form.author.data,id)
        return redirect(url_for("list_books_route"))
      except Exception as e:
         return render_template("edit_book.html" , form=form , error="Error : " + str(e)) , 400
    elif request.method == "GET":
      return render_template("edit_book.html" , form=bookform , book=book)

