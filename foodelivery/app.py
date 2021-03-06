"""
: Foodelivery App Entry point
export FLASK_ENV=development
export FLASK_APP=foodelivery/app.py
"""


from flask import Flask
from foodelivery.ext import site
from foodelivery.ext import toolbar
from foodelivery.ext import config
from foodelivery.ext import db
from foodelivery.ext import migrate
from foodelivery.ext import cli
from foodelivery.ext import auth
from foodelivery.ext import admin

def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
