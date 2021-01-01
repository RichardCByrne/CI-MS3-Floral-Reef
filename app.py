import os
from random import sample, randint
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
    try:
        return render_template("index.html")
    except:
        return render_template("404.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    try:
        query = request.form.get("query").lower()
        if not query.isalpha():
            flash("Invalid search query.")
        else:
            flowers = list(mongo.db.flowers.find({"$text": {"$search": query}}))
            return render_template("all_flowers.html", flowers=flowers)
    except:
        return render_template("404.html")


@app.route("/get_inspired")
def get_inspired():
    try:
        random_flower = {}
        # Referenced from https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html?highlight=aggregate#pymongo.database.Database.aggregate
        with mongo.db.flowers.aggregate([{"$sample": {"size": 1}}]) as cursor:
            for flower in cursor:
                random_flower = flower
        user_images = list(mongo.db.user_images.find({"flower_id": ObjectId(random_flower["_id"])}))
        if session:
            current_user = mongo.db.users.find_one({"email": session["user"]})
            current_user_images = list(mongo.db.user_images.find({"user_id": current_user["email"]}))
            return render_template("flower.html", flower=random_flower, user_images=user_images, current_user_images=current_user_images)
        else:
            return render_template("flower.html", flower=random_flower, user_images=user_images)
    except:
        return render_template("404.html")


@app.route("/all_flowers")
def get_all_flowers():
    try:
        flowers = list(mongo.db.flowers.find())
        return render_template("all_flowers.html", flowers=flowers)
    except:
        return render_template("404.html")


@app.route("/flower/<flower_id>")
def flower(flower_id):
    try:    
        flower = mongo.db.flowers.find_one({"_id": ObjectId(flower_id)})
        user_images = list(mongo.db.user_images.find({"flower_id": flower_id}))
        if session:
            current_user = mongo.db.users.find_one({"email": session["user"]})
            current_user_images = list(mongo.db.user_images.find({"user_id": ObjectId(current_user["_id"])}))
            current_user_created_flower = True if ObjectId(current_user["_id"]) == ObjectId(flower["created_by"]) else False
            print(current_user_created_flower)
            return render_template("flower.html", flower=flower, user_images=user_images, current_user_images=current_user_images, current_user_created_flower=current_user_created_flower)
        else:
            return render_template("flower.html", flower=flower, user_images=user_images)
    except:
        return render_template("404.html")


@app.route("/add_flower", methods=["GET", "POST"])
def add_flower():
    if request.method == "POST":
        try:
            db_length = len(list(mongo.db.flowers.find()))
            is_wildflower = "on" if request.form.get("is_wildflower") else "off"
            current_user = mongo.db.users.find_one({"email": session["user"]})
            new_flower = {
                "flower_name": request.form.get("flower_name"),
                "latin_name": request.form.get("latin_name"),
                "irish_name": request.form.get("irish_name"),
                "family": request.form.get("family"),
                "created_by": ObjectId(current_user["_id"]),
                "is_wildflower": is_wildflower,
                "flowering_time": request.form.get("flowering_time"),
                "image_url": request.form.get("image_url"),
                "description": request.form.get("description"),
                "location": request.form.get("location"),
                "occasions": request.form.get("occasions"),
                "affiliate_1": "https://howbertandmays.ie/",
                "affiliate_2": "https://www.knocknacarraflorists.ie/"
            }

            mongo.db.flowers.insert_one(new_flower)
            flash("Your flower has been added!\nThank you for your contribution.")
            return redirect(url_for("get_all_flowers"))
        except:
            return render_template("404.html")

    try:
        return render_template("add_flower.html")
    except:
        return render_template("404.html")


@app.route("/edit_flower/<flower_id>", methods=["GET", "POST"])
def edit_flower(flower_id):
    if request.method == "POST":
            current_user = mongo.db.users.find_one({"email": session["user"]})
            is_wildflower = "on" if request.form.get("is_wildflower") else "off"
            new_flower = {
                "flower_name": request.form.get("flower_name"),
                "latin_name": request.form.get("latin_name"),
                "irish_name": request.form.get("irish_name"),
                "family": request.form.get("family"),
                "created_by": ObjectId(current_user["_id"]),
                "is_wildflower": is_wildflower,
                "flowering_time": request.form.get("flowering_time"),
                "image_url": request.form.get("image_url"),
                "description": request.form.get("description"),
                "location": request.form.get("location"),
                "occasions": request.form.get("occasions"),
                "affiliate_1": "https://howbertandmays.ie/",
                "affiliate_2": "https://www.knocknacarraflorists.ie/"
            }

            mongo.db.flowers.update({"_id": ObjectId(flower_id)}, new_flower)
            flash("Flower successfully updated!")

            flower = mongo.db.flowers.find_one({"_id": ObjectId(flower_id)})
            user_images = list(mongo.db.user_images.find({"flower_id": ObjectId(flower["_id"])}))

            current_user = mongo.db.users.find_one({"email": session["user"]})
            current_user_images = list(mongo.db.user_images.find({"user_id": current_user["email"]}))
            return redirect(url_for("get_all_flowers"))
    try:
        flower = mongo.db.flowers.find_one({"_id": ObjectId(flower_id)})
        return render_template("edit_flower.html", flower=flower)
    except:
        return render_template("404.html")


@app.route("/delete_flower/<flower_id>")
def delete_flower(flower_id):
    try:
        mongo.db.flowers.remove({"_id": ObjectId(flower_id)})
        flash("Flower succesfully deleted")
        return redirect(url_for("get_all_flowers"))
    except:
        return render_template("404.html")


@app.route("/add_user_image/<flower_id>", methods=["GET", "POST"])
def add_user_image(flower_id):
    if request.method == "POST":
        try:
            user = mongo.db.users.find_one({"email": session["user"]})
            
            new_user_image = {
                "user_id": user["_id"],
                "flower_id": flower_id,
                "image_source": request.form.get("image_source"),
                "description": request.form.get("description")
            }
            mongo.db.user_images.insert_one(new_user_image)
            flash("Your image has been successfuly added!")
            return redirect(url_for("flower", flower_id=flower_id))
        except:
            return render_template("404.html")

    try:
        return render_template('add_user_image.html', flower_id=flower_id)
    except:
        return render_template("404.html")


@app.route("/delete_user_image/<image_id>")
def delete_user_image(image_id):
    try:
        mongo.db.user_images.remove({"_id": ObjectId(image_id)})
        flash("Your image has been deleted")
        return redirect(url_for("get_all_flowers"))
    except:
        return render_template("404.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
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
            return redirect(url_for("get_profile", email=session["user"]))
        except:
            return render_template("404.html")

    try:
        return render_template("register.html")
    except:
        return render_template("404.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
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
        except:
            return render_template("404.html")

    try:
        return render_template("/login.html")
    except:
        return render_template("404.html")


@app.route("/logout")
def logout():
    try:
        session.pop("user")
        flash("You have successfully been logged out.")
        return render_template("login.html")
    except:
        return render_template("404.html")


@app.route("/profile/<email>")
def get_profile(email):
    try:
        user = mongo.db.users.find_one(
            {"email": email}
        )
        current_user = mongo.db.users.find_one({"email": session["user"]})
        current_user_images = list(mongo.db.user_images.find({"user_id": current_user["_id"]}))
        return render_template("profile.html", name=user["first_name"], user_images=current_user_images)
    except:
        return render_template("404.html")


@app.route("/edit_profile/<email>", methods=["GET", "POST"])
def edit_profile(email):
    try:
        user = mongo.db.users.find_one(
        {"email": email}
        )
        if request.method == "POST":
            try:
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
            except:
                return render_template("404.html")

        return render_template("edit_profile.html", user=user)
        
    except:
        return render_template("404.html")


@app.route("/404")
def error404():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
