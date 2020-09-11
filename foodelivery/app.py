"""
: Foodelivery App Entry point
export FLASK_ENV=development
export FLASK_APP=foodelivery/app.py
"""


from flask import Flask
from foodelivery.ext import site
from foodelivery.ext import toolbar
from foodelivery.ext import config


def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
