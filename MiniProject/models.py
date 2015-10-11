from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import Required
from wtforms.fields.html5 import DateField
from wtforms_components import read_only
from MiniProject import client
from flask_material import Material
from werkzeug.security import check_password_hash,generate_password_hash
import json

db = client.calibrary

class MyForm(Form):
    uname = StringField('User Name', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    login = SubmitField('Login')

class Publication(Form):
    bookname = StringField('Book Name', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    publisher = StringField('Publisher', validators=[Required()])
    purchasedate = DateField('Purchase Date',validators=[Required()],format='%m/%d/%Y')
    price = IntegerField('Price',validators=[Required()])
    status = SelectField('Status',validators=[Required()],choices=[('av','Available'),('na','Not Available')])
    @staticmethod
    def addrecord(data):
        db.book.insert(data)
        return "Record added successfully"

class Book(Publication,Form):
    cd = IntegerField('CD',validators=[Required()])

class AddBook(Book):
    uadd = SubmitField('Add')

class UpdateBook(Book):
    id = StringField('Book ID', validators=[Required()])
    uupdate = SubmitField('Update')

    @staticmethod
    def update(id):
        calibrary = Database.connect()
        return calibrary.find_one({'_id':ObjectId(id)},{'_id':0})


class Circulation(Form):
    def issuebook():
        print ("ge")
    

class IssueBook(Form):
    studentid = StringField('Student ID',validators=[Required()])
    bookid = StringField('Book ID',validators=[Required()])
    issuedate = DateField('Issue Date',validators=[Required()])
    returndate = StringField('Return Date',validators=[Required()])
    issue = SubmitField('Issue')

class ReturnBook(Form):
    studentid = StringField('Student ID',validators=[Required()])
    bookid = StringField('Book ID',validators=[Required()])
    issuedate = DateField('Issue Date',validators=[Required()])
    returndate = StringField('Return Date',validators=[Required()])
    fine = StringField('Fine')   
    returnbook = SubmitField('Return')

class Reader(Form):
    id = StringField('Reader ID',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    name = StringField('Name',validators=[Required()])
    type = SelectField('Type',validators=[Required()],choices=[('Student','Student'),('Faculty','Faculty')])
    department = StringField('Department',validators=[Required()])
    register = SubmitField('Register')

    @staticmethod
    def change():
        oldpassword = PasswordField('Old Password',validators=[Required()])
        newpassword = PasswordField('New Password',validators=[Required()])
        confirmpassword = PasswordField('Confirm Password',validators=[Required()])

    def checkpassword(id,oldpassword,newpassword):
        temp = db.reader.find({id,oldpassword})
        if temp == None:
            return False
        else:
            generate_password_hash(newpassword,str='pbkdf2:sha1',int=8)
            return True