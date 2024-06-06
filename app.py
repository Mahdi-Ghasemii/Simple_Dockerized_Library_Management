from flask import Flask , render_template , request , redirect , url_for
from flask_mysqldb import MySQL
from wtforms import Form, validators, StringField, FloatField, IntegerField, DateField, SelectField

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = 'mahdi'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'LibraryApp'

mysql = MySQL()

@app.route('/')
def landing():
   return render_template("home.html")


if __name__ == '__main__':
   from routes.book import book_app
   from routes.member import user_app

   mysql.init_app(app)
   app.register_blueprint(book_app)
   app.register_blueprint(user_app)
   app.run(debug=True, host='0.0.0.0' , port=5001)





