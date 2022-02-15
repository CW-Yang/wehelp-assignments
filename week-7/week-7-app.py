from sys import prefix
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errors
from flask import Flask, request, redirect, render_template, session, Blueprint
from data import app2

app = Flask(__name__)

app.secret_key = "key"

@app.route('/')
def main():
    session["state"] = ""
    return render_template("index.html")

@app.route('/error/<error_message>')
def error(error_message):
    return render_template("error.html", error=error_message)

@app.route('/member/')
def membership():
    if(session["state"]=="SUCCESS"):
        return render_template("member.html", name=session["name"])
    else:
        return redirect('/')
    
app.register_blueprint(app2)

app.run(port=3000)