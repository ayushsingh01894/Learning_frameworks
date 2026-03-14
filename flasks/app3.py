from flask import Flask, render_template , request

#app3 is  file name main

app3 = Flask(__name__)

@app3.route("/")
def login():
    return render_template("login.html")

@app3.route("/submit" , methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username =="ayush123" and password == "123":
    #     return render_template("welcome.html" , name = username)
    # else:
    #     return "invalid"

    valid_users ={
        'admin':'123',
        'ayush123':'pass',
        'singh':'sin'
    }

    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html",name =username)
    else:
        return "invalid"

if __name__ == "__main__":
    app3.run(debug=True)