"""
: Foodelivery App Entry point
export FLASK_ENV=development
export FLASK_APP=foodelivery/app.py
"""


from flask import Flask
from foodelivery.ext import site


def create_app():
    """Factory to create a Flask app based on fatory pattern"""
    app = Flask(__name__)
    site.init_app(app)
    return app
