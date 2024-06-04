from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'mahdi'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'LibraryApp'


with app.app_context():
   f = open("./utils/user.sql", "r")
   query = f.read()
   mysql = MySQL(app)
   cursor = mysql.connection.cursor()
   cursor.execute(query)
   cursor.close()
   mysql.connection.commit()
