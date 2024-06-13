from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField

from app import mysql

class BookForm(Form):
   id = IntegerField("Id")
   title = StringField("Title")
   numPages = StringField("NumPages")
   author = StringField("Author")  


def select_all_books():
    cursor = mysql.connection.cursor()
    cursor.execute(''' select * from books''')
    books = cursor.fetchall()
    cursor.close()
    mysql.connection.commit()
    return books

def select_book_using_id(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id=%s" , [id])
    book = cursor.fetchone()
    cursor.close()
    return book

def insert_book(title , numPages , Author):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO books (title, NumPages, Author) values (%s,%s,%s);", (title,numPages,Author))
    cursor.close()
    mysql.connection.commit()


def delete_book(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s" , (id))
    cursor.close()
    mysql.connection.commit()


def update_book(title, numPages, Author, id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE books SET title=%s,numPages=%s,Author=%s WHERE id=%s" , [title,numPages,Author,id])
    book = cursor.fetchone()
    bookform = BookForm()
    cursor.close()
    mysql.connection.commit()
    return [book , bookform]


#---------------------------------------------------------------------------------------------


class MemberForm(Form):
   id = IntegerField("Id")
   name = StringField("Name")
   lastname = StringField("LastName")
   username = StringField("UserName")
   password = StringField("Password")
   phonenumber = StringField("PhoneNumber")
   address = StringField("Address")

def select_all_members():
    cursor = mysql.connection.cursor()
    cursor.execute(''' select * from users''')
    members = cursor.fetchall()
    cursor.close()
    mysql.connection.commit()
    return members

def insert_member(name, lastname, username, password, phonenumber, address):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (name, lastname, username, password, phonenumber, address) values (%s,%s,%s,%s,%s,%s);", [name, lastname, username, password, phonenumber, address])
    cursor.close()
    mysql.connection.commit()

def delete_member(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s" , [id])
    cursor.close()
    mysql.connection.commit()

def update_member(name,lastname,username,password,phonenumber,address,id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE users SET name=%s,lastname=%s,username=%s,password=%s,phonenumber=%s,address=%s WHERE id=%s" , [name,lastname,username,password,phonenumber,address,id])
    cursor.close()
    mysql.connection.commit()

def select_member_using_id(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id=%s" , [id])
    member = cursor.fetchone()
    memberform = MemberForm()
    cursor.close()
    return member


