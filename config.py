import os
from datetime import timedelta

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class ConfigClass(object):
    """ Flask application config """
    # Flask settings
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Flask-MongoEngine settings
    MONGO_DB_URL = os.environ.get("MONGO_URI_BR")
    MONGODB_SETTINGS = {
        'host': MONGO_DB_URL
    }

    # Flask-User settings
    # Shown in email templates and page footers
    USER_APP_NAME = "Book Repository"
    USER_ENABLE_EMAIL = True                    # Enable email authentication
    USER_ENABLE_USERNAME = True                 # Enable username authentication
    USER_ENABLE_CONFIRM_EMAIL = True            # Enable email after registration
    USER_ENABLE_FORGOT_PASSWORD = True          # Enable email after forgot password
    USER_ENABLE_CHANGE_PASSWORD = True          # Enable email after password change
    USER_SEND_PASSWORD_CHANGED_EMAIL = True     # Enable email after password change
    USER_REQUIRE_RETYPE_PASSWORD = True
    USER_ENABLE_CHANGE_USERNAME = False

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    # TLS Port: 587, SSL Port: 465 --> TLS or SSL: True/False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    USER_EMAIL_SENDER_EMAIL = os.environ.get("USER_EMAIL_SENDER_EMAIL")

    # Flask Session Configuration for Session Protection and "Remember Me" function
    SESSION_PROTECTION = "strong"
    REMEMBER_COOKIE_DURATION = timedelta(seconds=3600)   # Logged out after 1 hour (come back in without logging in too)
    SESSION_COOKIE_SECURE = True

    # Flask User Manager Configuration
    USER_COPYRIGHT_YEAR = 2020
    USER_CORPORATION_NAME = "GaffCo Consulting"
