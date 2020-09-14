import click # noqa
from foodelivery.ext.db import db
from foodelivery.ext.db import models # noqa


def init_app(app):
    @app.cli.command()
    def create_db():
        """Database initialization"""
        db.create_all()


    @app.cli.command()
    def list_orders():
        click.echo("List of orders")

