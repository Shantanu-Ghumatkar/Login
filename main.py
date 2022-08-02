from email import message
import email
from webbrowser import get
import mysql.connector
from flask import Flask, render_template, request,redirect,session, url_for
import sys
import os
import traceback

app = Flask(__name__ ,static_url_path='/static')
app.secret_key=os.urandom(24)
try:
            conn = mysql.connector.connect(host ="localhost", user="root", 
            password="",database="log_in")
            mycursor =conn.cursor()
except:
            print("Some error occured. could not connect. connect to the my sql")
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

@app.route('/Contact_us',methods=['POST'])
def Contact_us():
    email=request.form.get('email')
    message=request.form.get('message')

    try:
        mycursor.execute("""
        update users set messege='{}' where Email like '{}';
        """.format(message,email))
        conn.commit()
        data =mycursor.fetchall()

    except Exception as e:
        return render_template('welcome.html')
    else:
        return "done"

@app.route('/Forgotten')
def Forgotten():
    return render_template('Forgotten.html')

@app.route('/Forgotten_P1/<score>')
def Forgotten_P1(score):
   
    if score==" ":
        score='No User exist'
    else:
        score='Your Password is'+score
    # exp={'score':score,'res':res}
    # return render_template('result.html',result=exp)
    
    return render_template('pass.html', pa=score)

@app.route('/Forgotten_P',methods=['POST','GET'])
def Forgotten_P():
    email=request.form.get('email')
    mycursor.execute("""
            SELECT * FROM `users` WHERE Email like '{}';
            """.format(email))
    data =mycursor.fetchall()
    res='Forgotten_P1'
    if data:
        score=data[0][3]
        score1=data[0][2]
        print(score1 + 'psss is ' +score )
        return redirect(url_for('Forgotten_P1',score=data[0][3]))
    else:
            return redirect(url_for('Forgotten_P1',score=' '))

if __name__ =="__main__":
    app.run(debug=True)