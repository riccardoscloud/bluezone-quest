import os
import sqlalchemy
import requests
import json

from flask import Flask, redirect, render_template, request, url_for, Response
from sqlalchemy import create_engine
from dotenv import load_dotenv
from datetime import datetime

# SETUP: Load .env
load_dotenv()

# SETUP: Application
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# SETUP: SQLAlchemy
db = create_engine("sqlite:///database.db")

# APP ROUTES #
# Homepage
@app.route("/")
def index():
    # Simple GET page, with content displayed conditionally of session
    return render_template("/index.html")

# Homepage
@app.route("/faq")
def index():
    # Simple GET page, with content displayed conditionally of session
    return render_template("/faq.html")

# Homepage
@app.route("/privacy")
def index():
    # Simple GET page, with content displayed conditionally of session
    return render_template("/privacy.html")

# Homepage
@app.route("/terms")
def index():
    # Simple GET page, with content displayed conditionally of session
    return render_template("/terms.html")
