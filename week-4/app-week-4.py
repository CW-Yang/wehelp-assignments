from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app = Flask(__name__)

app.secret_key = "key"

# Login page/ Main page
@app.route("/")
def main():
    session["state"] = ""
    return render_template("index.html")

# Authentication
@app.route("/signin", methods=['POST'])
def check():
    user_account = request.form["account"]
    user_password = request.form["password"]
    answer = "test"
    # print(user_account)
    # print(user_password)

    if(user_account == answer and user_password == answer):
        state = "SUCCESS"
    elif(user_account == "" or user_password == ""):
        state = "EMPTY"       
    else:
        state = "WRONG"
    
    session["state"] = state
    
    # check state
    if(state == "SUCCESS"):
        return redirect("/member/")
    elif(state == "WRONG"):
        return redirect("/error/?message=帳號或密碼輸入錯誤")
    elif(state == "EMPTY"):
        return redirect("/error/?message=請輸入帳號、密碼")

    
# Login successfully
@app.route("/member/")
def membership():
    if(session["state"] == "SUCCESS"):
        return render_template("membership.html")
    else:
        return redirect("/")
    

# Login failed
@app.route("/error/")
def error():
    message = request.args.get("message", "")
    return render_template("errorMsg.html", errMsg=message)

app.run(port=3000)




