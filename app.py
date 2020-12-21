import os
from flask import (Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DMNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/all_flowers")
def get_all_flowers():
    flowers = list(mongo.db.flowers.find())
    return render_template("all_flowers.html", flowers=flowers)


@app.route("/flower/<flower_id>")
def flower(flower_id):
    flower = mongo.db.flowers.find_one({"_id": ObjectId(flower_id)})
    return render_template("flower.html", flower=flower)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Email already in use.")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower()
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("email").lower()
        flash("Registration successful!")
        # return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = existing_user["email"].lower()
                flash("Welcome, {}".format(existing_user["first_name"].capitalize()))
                return redirect(url_for("get_profile", email=existing_user["email"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("/login.html")


@app.route("/logout")
def logout():
    session.pop("user")
    flash("You have successfully been logged out.")
    return render_template("login.html")


@app.route("/profile/<email>")
def get_profile(email):
    user = mongo.db.users.find_one(
        {"email": email}
    )
    return render_template("profile.html", name=user["first_name"])


@app.route("/edit_profile/<email>", methods=["GET", "POST"])
def edit_profile(email):
    user = mongo.db.users.find_one(
        {"email": email}
    )
    if request.method == "POST":
        record_update = {
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name")
        }

        mongo.db.users.update({"email": email}, record_update)
        session["user"] = request.form.get("email")
        flash("Details Successfully Updated")
        return redirect(url_for("get_profile", email=session["user"]))

    return render_template("edit_profile.html", user=user)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
