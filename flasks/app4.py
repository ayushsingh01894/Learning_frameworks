from flask import Flask,render_template ,request

app4 = Flask(__name__)

@app4.route("/")
def home():
    return render_template("home.html")

@app4.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app4.run(debug=True)



# combining home, base1 ,about .hmtl and app4 then run result shown in browser