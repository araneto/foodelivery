"""
export FLASK_ENV=development
export FLASK_APP=foodelivery/app.py
"""


from flask import Flask


def create_app():
    """Factory to create a Flask app based on fatory pattern"""
    app = Flask(__name__)
    return app
