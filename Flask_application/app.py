from flask import Flask,render_template,request,flash,redirect,url_for
import sqlite3

app = Flask(__name__)

#con=sqlite3.connect("databse.db")
#con.execute("CREATE TABLE IF NOT EXISTS data(name TEXT,email text,contact INTEGER,password TEXT,password1 TEXT")
#con.close()
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__=='main':
    app.run(debug=True)
