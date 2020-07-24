import os
from flask import Flask, render_template_string, render_template
from flask_mongoengine import MongoEngine
from flask_user import login_required, UserManager, UserMixin, current_user, roles_required


from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# Class-based application configuration (move to separate configuration file)


class ConfigClass(object):
    """ Flask application config """
    # Flask settings
    SECRET_KEY = os.urandom(128).hex()
    print("Random Secret Key:", SECRET_KEY)
    CSRF_ENABLED = True

    # Flask-MongoEngine settings
    MONGO_DB_URL = os.getenv("MONGO_URI_FU")
    print("MongoDB URL:", MONGO_DB_URL)
    MONGODB_SETTINGS = {
        'host': MONGO_DB_URL
    }

    # Flask-User settings
    # Shown in email templates and page footers
    USER_APP_NAME = "Book Repository"
    USER_ENABLE_EMAIL = True      # Enable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = True

    # USER_AFTER_LOGIN_ENDPOINT = 'main.member_page'
    # USER_AFTER_LOGOUT_ENDPOINT = 'main.home_page'

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    # TLS Port: 587, SSL Port: 465 --> TLS or SSL: True/False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = ("Naoise Gaffney - 'Gaff'",
                           "forms.email4pythonandjs@gmail.com")
    USER_EMAIL_SENDER_EMAIL = "forms.email4pythonandjs@gmail.com"


""" # User Profile Customisation
class CustomUserProfileForm(UserProfileForm):
    # Add a country field to the UserProfile form
    country = StringField(_('Country'), validators=[DataRequired()]) """


def create_app():
    """ Flask application factory """

    # Setup Flask and load app.config
    app = Flask(__name__)
    app.config.from_object(__name__+'.ConfigClass')

    # Setup Flask-MongoEngine
    db = MongoEngine(app)

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

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        # String-based templates
        return render_template_string("""
            {% extends "flask_user_layout.html" %}
            {% block content %}
                <h2>Home page</h2>
                <p><a href={{ url_for('user.register') }}>Register</a></p>
                <p><a href={{ url_for('user.login') }}>Sign in</a></p>
                <p><a href={{ url_for('home_page') }}>Home page</a> (accessible to anyone)</p>
                <p><a href={{ url_for('member_page') }}>Member page</a> (login required)</p>
                <p><a href={{ url_for('user.logout') }}>Sign out</a></p>
            {% endblock %}
            """)

    # The Members page is only accessible to authenticated users via the @login_required decorator
    @app.route('/members')
    @login_required    # User must be authenticated
    def member_page():
        # String-based templates
        return f'<h3>Welcome, {current_user.username}</h3>' + render_template_string("""
            {% extends "flask_user_layout.html" %}
            {% block content %}
                <h2>Members Page</h2>
                <p><a href={{ url_for('user.register') }}>Register</a></p>
                <p><a href={{ url_for('user.login') }}>Sign in</a></p>
                <p><a href={{ url_for('home_page') }}>Home page</a> (accessible to anyone)</p>
                <p><a href={{ url_for('member_page') }}>Member page</a> (login required)</p>
                <p><a href={{ url_for('user.logout') }}>Sign out</a></p>
            {% endblock %}
            """)

    @app.route("/admin")
    @roles_required("admin")
    def admin_dashboard():
        return "Admin Dashboard"

    return app


# export PRODUCTION=ON | OFF in TEST
# PRODUCTION App -> Settings -> Reveal Config Vars -> KEY: PRODUCTION, VALUE: ON
if __name__ == "__main__":
    app = create_app()
    if os.environ.get("PRODUCTION") == "ON":
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=False)
    else:
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=True)
