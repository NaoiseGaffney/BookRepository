import os
from flask import Flask, render_template_string, render_template, redirect, url_for
from flask_mongoengine import MongoEngine, MongoEngineSession, MongoEngineSessionInterface
from flask_user import login_required, UserManager, UserMixin, current_user, roles_required
from wtforms.validators import DataRequired
from mongoengine.errors import NotUniqueError
from statistics import mean


# generates WTForms from MongoEngine models
from flask_mongoengine.wtf import model_form


from config import ConfigClass

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


""" Flask application factory """

# Setup Flask and load app.config
app = Flask(__name__, static_folder="static")
app.config.from_object(__name__+".ConfigClass")

# Setup Flask-MongoEngine
db = MongoEngine(app)

# Use Flask Sessions with Mongoengine
app.session_interface = MongoEngineSessionInterface(db)


class User(db.Document, UserMixin):
    # Active set to True to allow login of user
    active = db.BooleanField(default=True)

    # User authentication information
    username = db.StringField(default="")
    password = db.StringField()

    # User information
    first_name = db.StringField(default="")
    last_name = db.StringField(default="")
    email = db.StringField(default="")
    email_confirmed_at = db.DateTimeField()
    # Required for the e-mail confirmation, and subsequent login.

    # Relationships
    roles = db.ListField(db.StringField(), default=["user"])

    meta = {
        "auto_create_index": True,
        "index_background": True,
        "indexes": ["username"]
    }


class Book(db.Document):
    title = db.StringField(default="")
    author = db.StringField(default="")
    year = db.IntField(default="")
    ISBN = db.StringField(default="123-1-123-12345-1", unique=True)
    short_description = db.StringField()
    user = db.ReferenceField(User, required=True)
    comments = db.ListField()
    votes = db.ListField(db.IntField(choices=[1, 2, 3, 4, 5]))
    rating = db.FloatField()  # book.calc_votes()

    def calc_votes(self):
        self.rating = mean(n for n in self.votes if n is not None)

    # Single indexes created for "status" and "created_at", indexing in the background
    # Compound indexes [("")]
    meta = {
        # "collection":"VirtualBook" # Renaming the collection name in MongoDB
        "auto_create_index": True,
        "index_background": True,
        # "indexes": ["status", "created_at"]
        # "indexes":[("status", "created_at"), ("title",)]
        # "indexes": [
        #     {
        #         "name": "status",
        #         "fields": ("status", "created_at",)
        #     }, {
        #         "name": "title",
        #         "fields": ("title",),
        #         "unique": True
        #     }]
    }


# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)


# The Home page is accessible to anyone


@app.route("/")
def home_page():
    if current_user.is_authenticated:
        return redirect(url_for("member_page"))
    return render_template("index.html")


# The Members page is only accessible to authenticated users via the @login_required decorator


@app.route("/members")
@login_required    # User must be authenticated
def member_page():
    return render_template("members.html")


# The Admin page requires an 'Admin' role.
@ app.route("/admin")
@ roles_required("Admin")  # Use of @roles_required decorator
def admin_page():
    return render_template("admin.html")


@app.route("/user/<int:id>/")
def user_profile(id):
    return f"Profile page of user #{id}"


# export PRODUCTION=ON | OFF in TEST
# PRODUCTION App -> Settings -> Reveal Config Vars -> KEY: PRODUCTION, VALUE: ON
if __name__ == "__main__":
    if os.environ.get("PRODUCTION") == "ON":
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=False)
    else:
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=True)
