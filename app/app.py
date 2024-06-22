from flask import Flask , render_template , request , redirect , url_for
from flask_mysqldb import MySQL
from wtforms import Form, validators, StringField, FloatField, IntegerField, DateField, SelectField

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'mahdi'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'LibraryApp'
app.config['MYSQL_PORT'] = 3306


mysql = MySQL()

@app.route('/')
def landing():
   return render_template("index.html")


if __name__ == '__main__':
   from routes.book import book_app
   from routes.member import user_app

   mysql.init_app(app)
   app.register_blueprint(book_app)
   app.register_blueprint(user_app)
   app.run(debug=True, host='0.0.0.0' , port=4000)





