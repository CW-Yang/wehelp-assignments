import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errors
from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = "key"

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="website"
# )
config = {
    "host":"localhost",
    "user":"root",
    "password":"root",
    "database":"website"
}

connection_pool = MySQLConnectionPool(pool_name='my_connection_pool',
                                     pool_size=5,
                                     **config)

# private function
def connect_database(command, value, data_modified):
    try:
        mydb = connection_pool.get_connection()
        myCursor = mydb.cursor()
        myCursor.execute(command, value)
        result = myCursor.fetchall()

        if(data_modified):
            mydb.commit()
    except errors.Error as e:
        print(e)
    finally:
        mydb.close()
        myCursor.close()
        return result

def isSuccess(account, password):
    command = "SELECT * FROM member WHERE username = %s AND password = %s"
    value = (account, password)
    result = connect_database(command, value, False)

    if(result != None and result != []):
        return True

    return False

def isEmpty(account, password):
    return(account == "" or password == "")

def isReapt(unsign_account):
    command = "SELECT * FROM member WHERE username = %s"
    value = (unsign_account, )
    result = connect_database(command, value, False)

    if(result != None and result != []):
        return True

    return False

def insert_record(name, account, password):
    command = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    value = (name, account, password)
    result = connect_database(command, value, True)
    return result

def get_user_name(account):
    command = "SELECT name FROM member WHERE username = %s"
    value = (account, )
    data = connect_database(command, value, False)
    data = tuple(data[0])[0]

    return data

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
        return redirect(url_for('error', error_message="帳號已被註冊"))
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
        return redirect(url_for('membership'))
    elif(isEmpty(account, password)):
        session["state"] = "EMPTY"
        return redirect(url_for('error', error_message="請輸入帳號或密碼"))
    else:
        session["state"] = "WRONG"
        return redirect(url_for('error', error_message="帳號或密碼輸入錯誤"))

# Login successfully
@app.route("/member/")
def membership():
    if(session["state"] == "SUCCESS"):
        return render_template("response.html", subject="歡迎光臨，這是會員頁", Msg=session["name"]+"，歡迎登入系統", return_text="登出系統")
    else:
        return redirect("/")

# Login failed
@app.route("/error/<error_message>")
def error(error_message):
    return render_template("response.html", subject="失敗頁面", Msg=error_message, return_text="返回首頁")

app.run(port=3000)
