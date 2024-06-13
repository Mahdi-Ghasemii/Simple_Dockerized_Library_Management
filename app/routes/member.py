from flask import Blueprint, Flask , render_template , request , redirect , url_for
from flask_mysqldb import MySQL
from wtforms import Form, validators, StringField, FloatField, IntegerField, DateField, SelectField
from models.model import *

user_app = Blueprint('user', __name__, template_folder='templates')


@user_app.route('/members')
def list_members_route():
      members = select_all_members()
      return render_template("members.html" , members=members)


@user_app.route('/add_member' , methods={"GET" , "POST"})
def add_member_route():
    if request.method == "POST":
      form = MemberForm(request.form)
      insert_member(form.name.data,form.lastname.data,form.username.data,form.password.data,form.phonenumber.data,form.address.data)
      return redirect(url_for("user.list_members_route"))
    elif request.method == "GET":
      form = MemberForm()
      return render_template("add_member.html" , form=form)
    

# @user_app.route('/delete_member' , defaults={'id':None}, methods={"POST"})
@user_app.route('/delete_member' , methods={"POST"})
def delete_member_route():
    id = request.args.get('id')
    delete_member(id)
    return redirect(url_for("user.list_members_route"))


@user_app.route('/edit_member/<id>' , methods={"GET" , "POST"})
def edit_member_route(id):
    cursor = mysql.connection.cursor()
    if request.method == "POST":
      form = MemberForm(request.form)
      update_member(form.name.data,form.lastname.data,form.username.data,form.password.data,form.phonenumber.data,form.address.data,id)
      return redirect(url_for("user.list_members_route"))

    elif request.method == "GET":
      memberform = MemberForm()
      member = select_member_using_id(id)
      return render_template("edit_member.html" , form=memberform , member=member)