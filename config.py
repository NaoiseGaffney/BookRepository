import os
from datetime import timedelta

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class ConfigClass(object):
    """ Flask application config """
    # Flask settings
    SECRET_KEY = os.urandom(128).hex()
    print("Random Secret Key:", SECRET_KEY)
    # CSRF_ENABLED = True

    # Flask-MongoEngine settings
    MONGO_DB_URL = os.getenv("MONGO_URI_BR")
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

    # Flask Session Configuration for Session Protection and "Remember Me" function
    SESSION_PROTECTION = "strong"
    REMEMBER_COOKIE_DURATION = timedelta(seconds=3600) # Logged out after 1 hour (come back in without logging in too)

    # Flask User Manager Configuration
    USER_COPYRIGHT_YEAR = 2020
    USER_CORPORATION_NAME = "GaffCo Consulting"
