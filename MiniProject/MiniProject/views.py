'''Imports'''
from datetime import datetime
from functools import wraps
from flask import render_template,flash,get_flashed_messages,request,redirect,url_for,jsonify,make_response
from flask_login import login_required,login_user,logout_user,current_user
from MiniProject import app,client
from User import *
from models import *

'''Handle Unauthorized Request'''
@login_manager.unauthorized_handler
def unauthorized_callback():
    form = MyForm()
    flash('Please log in first')
    return render_template('login.html',title="Login",message='Please login to continue',form=form,year=datetime.now().year) 

'''Routes'''

'''Main'''
@app.route('/')
def index():
    return render_template('index.html',title="Home",message='Welcome to CA Library',year=datetime.now().year)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
         form = MyForm()
         return render_template('login.html',title="Login",message='Please login to continue',form=form,year=datetime.now().year) 
    elif request.method == 'POST':
        user = User.get(request.form['uname'])
        if(user == None):
            form = MyForm()
            flash('User Name does not exist')
            return render_template('login.html',title="Login",message='Please login to continue',form=form,year=datetime.now().year)
        elif (user and User.validate_login(request.form['password'])):
            login_user(user)
            return redirect(url_for('home'))
        else:
            form = MyForm()
            flash('Invalid Credentials')
            return render_template('login.html',title="Login",message='Please login to continue',form=form,year=datetime.now().year)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('index'))


@app.route('/home')
@login_required
def home():
    return render_template(
           'home.html',
            title=current_user.id,
            year=datetime.now().year
        )

'''Cataloging'''
@app.route('/addbook',methods=['GET', 'POST'])
@login_required
def addbook():
    if request.method == 'GET':
        form = AddBook()
        return render_template('addbook.html',
                                title='Add Book',
                                form=form,
                                year=datetime.now().year)
    else:
        bookname = request.form['bookname']
        author = request.form['author']
        publisher = request.form['publisher']
        date = request.form['purchasedate']
        price = request.form['price']
        cd = request.form['cd']
        status = request.form['status']
        data = {"bookname":bookname,"author":author,"publisher":publisher,"date":date,"price":price,"cd":cd,"status":status}
        flash (Publication.addrecord(data))
        return redirect(url_for('addbook'))

@app.route('/updatebook',methods=['GET', 'POST'])
def updatebook():
    if request.method == 'GET':
        form = UpdateBook()
        return render_template('updatebook.html',
                                title='Update Book',
                                updt=0,
                                form = form,
                                year=datetime.now().year)
    else:
        id = request.form['id']
        data = UpdateBook.update(id)
        if data == None:
            flash("No Book With This Record")
            return redirect(url_for('updatebook'))
        else:
            return jsonify(data)

@app.route('/update',methods=['POST','GET'])
@login_required       
def update():
    bookid = request.form.get('bookid')
    bookname = request.form.get('bookname')
    author = request.form.get('author')
    publisher = request.form.get('publisher')
    date = request.form.get('date')
    price = request.form.get('price')
    cd = request.form.get('cd')
    status = request.form.get('status')
    data = {"responce" : str(1)}
    return jsonify(data)

'''Circulation'''
@app.route('/issuebook',methods=['POST','GET'])
@login_required
def issuebook():
    if request.method == 'GET':
        form = IssueBook()
        return render_template('issuebook.html',title='Issue Book',form=form,year=datetime.now().year)
    elif request.method == 'POST':
        bookid = request.form.get('bookid')
        studentid = request.form.get('studentid')
        issuedate = request.form.get('issuedate')
        returndate = request.form.get('returndate')
        flash('Book Issued Successfully')
        return redirect(url_for('issuebook'))
    else:
        flash('Something went wrong')
        return redirect(url_for('issuebook'))
    
@app.route('/returnbook')
@login_required
def returnbook():
    form = ReturnBook()
    return render_template('returnbook.html',
         title='Return Book',
         form = form,
         year=datetime.now().year)

'''Reader Management'''

'''Profile'''
app.route('/changepassword',methods = ['GET','POST'])
def changepassword():
    if request.method == 'GET':
        Reader = Reader.change()
        return render_template('changepassword.html',title='Change Password',
                                form=Reader,
                                year=datetime.now().year)
    else:
        oldpassword = request.form['oldpassword']
        newpassword = request.form['newpassword']
        if Reader.checkpassword(current_user.id,oldpassword,newpassword):
            flash('Yay')
        else:
            flash('Gm')
            return redirect(url_for('changepassword'))

@app.route('/addreader',methods=['GET', 'POST'])
@login_required
def addreader():
    if request.method == 'GET':
        form = Reader()
        return render_template('addreader.html',
                                title='Add Reader',
                                form=form,
                                year=datetime.now().year)
    else:
        bookname = request.form['bookname']
        author = request.form['author']
        publisher = request.form['publisher']
        date = request.form['purchasedate']
        price = request.form['price']
        cd = request.form['cd']
        status = request.form['status']
        data = {"bookname":bookname,"author":author,"publisher":publisher,"date":date,"price":price,"cd":cd,"status":status}
        flash (Publication.addrecord(data))
        return redirect(url_for('addbook'))