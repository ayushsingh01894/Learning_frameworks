""" from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello user'

@app.route("/contect")
def contect():
    return 'Hello contect'

@app.route("/about")
def about():
    return 'Hello about'

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "you send data"
    else:
        return "you are only viewing"

if __name__ == "__main__":
    app.run(debug=True) """

from flask import Flask ,request,redirect,url_for,Response,session

app = Flask(__name__)
app.secret_key="supersecret"

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username =="admin" and password =="123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("in-valid credentail. try again", mimetype="text/plain")

    return '''
    <h2>Login Page</h2>
    <form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
    </form>
'''       
#welcome page (after login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome.{session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>
'''
    return redirect(url_for("login"))

#logout route

@app.route("/logout")
def logout():
    session.pop("user", None)#session["user"]="ayush"
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)