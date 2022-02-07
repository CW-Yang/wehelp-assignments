import mysql.connector
from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.secret_key = "key"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="website"
)

myCursor = mydb.cursor()

# private function
def isSuccess(account, password):
    myCursor.execute("SELECT username, password FROM member")
    result = myCursor.fetchall()

    answer = (account, password)
    for target in result:
        if(target == answer):
            return True

    return False

def isEmpty(account, password):
    return(account == "" or password == "")

def isReapt(unsign_account):
    myCursor.execute("SELECT username FROM member")
    result = myCursor.fetchall()

    for target in result:
        if(str(target).strip('(),\'') == unsign_account):
            return True

    return False

def insert_record(name, account, password):
    command = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    value = (name, account, password)
    myCursor.execute(command, value)
    mydb.commit()

def get_user_name(account):
    command = "SELECT name FROM member WHERE username = %s"
    username = (account, )
    myCursor.execute(command, username)
    result = myCursor.fetchone()
    result = str(result).strip('(),\'')

    return result

# Main Page
@app.route("/")
def main():
    session["state"] = ""
    return render_template("index.html")

@app.route("/signup", methods=['POST'])
def sign_up():
    name = request.form["name"]
    account = request.form["unsign_account"]
    password = request.form["unsign_password"]

    if(isReapt(account)):
        return redirect("/error/?message=帳號已經被註冊")
    else:
        insert_record(name, account, password)
        return redirect("/")

@app.route("/signin", methods=['POST'])
def check():
    account = request.form["account"]
    password = request.form["password"]

    if(isSuccess(account, password)):
        session["name"] = get_user_name(account)
        session["state"] = "SUCCESS"
        return redirect("/member/")
    elif(isEmpty(account, password)):
        session["state"] = "EMPTY"
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        session["state"] = "WRONG"
        return redirect("/error/?message=帳號或密碼輸入錯誤")

# Login successfully
@app.route("/member/")
def membership():
    if(session["state"] == "SUCCESS"):
        return render_template("membership.html", name=session["name"])
    else:
        return redirect("/")

# Login failed
@app.route("/error/")
def error():
    message = request.args.get("message", "")
    return render_template("errorMsg.html", errMsg=message)

app.run(port=3000)
