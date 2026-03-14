from flask import Flask,render_template ,request

app5 = Flask(__name__)

@app5.route("/feedback",methods=["POST" ,"GET"])
def feedback():
    if request.method == "POST":
        #read data 
        name = request.form.get("username")
        message = request.form.get("message")
        return render_template("thankyou.html", user=name, message=message)
    return render_template("feedback.html")


if __name__ == "__main__":
    app5.run(debug=True)


# feedback , thankyou base .html and this file 