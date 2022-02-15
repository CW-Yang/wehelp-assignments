from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errors
from flask import Flask, request, redirect, render_template, session, Blueprint, url_for

app2 = Blueprint('app2', __name__)

app2.secret_key = "key"

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
def compare_with_database(command, value, data_modified):
    try:
        mydb = connection_pool.get_connection()
        my_cursor = mydb.cursor()
        my_cursor.execute(command, value)
        result = my_cursor.fetchall()

        if(data_modified == True):
            mydb.commit()
            result = my_cursor.rowcount
    except errors.Error as e:
        print(e)
    finally:
        mydb.close()
        my_cursor.close()
        return result

def is_success(username, password):
    command = "SELECT * FROM member WHERE username = %s AND password = %s"
    value = (username, password)
    result = compare_with_database(command, value, False)

    if(result != None and result != []):
        return True
    
    return False

def is_empty(username, password):
    return(username == "" or password == "")

def is_reapt(unsign_username):
    command = "SELECT * FROM member WHERE username = %s"
    value = (unsign_username, )
    result = compare_with_database(command, value, False)

    if(result != None and result != []):
        return True

    return False

def insert_record(name, username, password):
    command = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    value = (name, username, password)
    result = compare_with_database(command, value, True)
    return result

def get_user_name(username):
    command = "SELECT name FROM member WHERE username = %s"
    value = (username, )
    data = compare_with_database(command, value, False)   
    data = tuple(data[0])[0]

    return data

def get_member_data_formatting(username):
    command = "SELECT id, name, username FROM member WHERE username = %s"
    value = (username, )
    data = compare_with_database(command, value, False)

    if(data != []):
        data = tuple(data[0])
        result = {
            "data":{
                "id":data[0],
                "name":data[1],
                "username":data[2]
            }
        }
    else:
        result = {
            "data":None
        }
    return result

def update_data(new_data, username):
    command = "UPDATE member SET name = %s WHERE username = %s"
    value = (new_data, username)
    result = compare_with_database(command, value, True)

    return result

def get_response_formatting(state):
    result = {
        state:True
    }
    return result

@app2.route('/signup', methods=['POST'])
def sign_up():
    name = request.form["name"]
    username = request.form["unsign_username"]
    password = request.form["unsign_password"]

    if(is_reapt(username)):
        return redirect(url_for('error', error_message="帳號已被註冊"))
    else:
        insert_record(name, username, password)
        return redirect("/")

@app2.route('/signin', methods=['POST'])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]

    if(is_success(username, password)):
        session["name"] = get_user_name(username)
        session["username"] = username
        session["state"] = "SUCCESS"
        return redirect(url_for('membership'))
    elif(is_empty(username, password)):
        return redirect(url_for('error', error_message="請輸入帳號或密碼"))
    else:
        return redirect(url_for('error', error_message="帳號或密碼輸入錯誤"))

@app2.route('/api/members')
def search_members():
    username = request.args.get('username')
    result = get_member_data_formatting(username)

    return result

@app2.route('/api/member', methods=['POST'])
def renew_name():
    data = request.get_json()
    new_name = data["name"]
    username = session["username"]
    result = update_data(new_name, username)

    if(session["state"] == "SUCCESS"):
        if(result == 1):
            result = get_response_formatting("ok")
            session["name"] = new_name
        else:
            result = get_response_formatting("error")
    else:
        result = get_response_formatting("error")
    
    return result


