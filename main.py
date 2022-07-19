

import email
from re import I
from unicodedata import name
from flask import Flask, render_template, request,redirect,session
import sys
import mysql.connector
import os


app = Flask(__name__)
app.secret_key=os.urandom(24)
try:
            conn = mysql.connector.connect(host ="localhost", user="root", 
            password="",database="log_in")
            mycursor =conn.cursor()
except:
            print("Some error occured. could not connect")
            sys.exit(0)
else:
            print("-----Connected to database------- ")

@app.route('/')
def login():
    return render_template('login.html')
   

@app.route('/register')
def about():
        return render_template('register.html')



@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    mycursor.execute("""
            SELECT * FROM `users` WHERE Email like '{}' and Password like '{}';
            """.format(email,password))
    data =mycursor.fetchall()
    if data:
            session['user_id']=data[0][0]
            return redirect('/home')
    else:
            return redirect('/')


@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')
    try:
        mycursor.execute("""
        INSERT INTO users (ID, Name, Email, Password) VALUES (NULL, '{}', '{}', '{}');
        """.format(name,email,password))
        conn.commit()
        mycursor.execute("""
            SELECT * FROM `users` WHERE Email like '{}' ;
            """.format(email))
        data =mycursor.fetchall()

    except:
        return redirect('/register')
    else:
            session['user_id']=data[0][0]
            return redirect('/home')


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


if __name__ =="__main__":
    app.run(debug=True)