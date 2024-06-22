from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

dirname = os.path.dirname(__file__)


app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'mahdi'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_PORT'] = 3306
app.config['HOST_IP'] = '0.0.0.0'

with app.app_context():
   filename = os.path.join(dirname, 'script.sql')
   f = open(filename, "r")
   query = f.read()
   mysql = MySQL(app)
   cursor = mysql.connection.cursor()
   cursor.execute(query)
   cursor.close()
   mysql.connection.commit()
   app.config['MYSQL_DB'] = 'LibraryApp'
