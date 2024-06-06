from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = 'mahdi'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['HOST_IP'] = '0.0.0.0'
# app.config.setdefault("MYSQL_UNIX_PORT")

with app.app_context():
   f = open("./utils/script.sql", "r")
   query = f.read()
   mysql = MySQL(app)
   cursor = mysql.connection.cursor()
   cursor.execute(query)
   cursor.close()
   mysql.connection.commit()
   app.config['MYSQL_DB'] = 'LibraryApp'
