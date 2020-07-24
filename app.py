import os
import gunicorn
from flask import Flask

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / (".env")
load_dotenv(dotenv_path=env_path)


app = Flask(__name__)


@app.route("/")
def hello():
    if os.environ.get("PRODUCTION") == "ON":
        return "Hello, World! This Flask application is running in PRODUCTION (debug=False)."
    else:
        return "Hello, World! This Flask application is running in DEVELOPMENT or STAGING (debug=True)."


if __name__ == "__main__":
    if os.environ.get("PRODUCTION") == "ON":
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=False)
    else:
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=True)
