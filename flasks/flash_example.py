from flask import Flask,render_template ,request,redirect,url_for,flash
flash_example = Flask(__name__)
flash_example.secret_key ="my-secret-key"

@flash_example.route("/",methods=["POST" ,"GET"])
def form():
    if request.method == "POST":
        #read data 
        name = request.form.get("name")
        if not name:
            flash("Name cannot be empty")
            return render_template(url_for("form"))
        flash(f"thank{name}, your feedback was saved")
        return redirect(url_for("thankyouu"))
    return render_template("form.html")

@flash_example.route("/thankyouu")
def thankyouu():
    return render_template("thankyouu.html")


if __name__ == "__main__":
    flash_example.run(debug=True)


# thankyouu , form , base3 