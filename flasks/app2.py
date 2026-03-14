from flask import Flask , render_template , request

app2 = Flask(__name__)

@app2.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name = "ayush",
        is_topper =True,
        subjects =["Maths", "Science","History"]
    )



if __name__ == "__main__":
    app2.run(debug=True)