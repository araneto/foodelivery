import click # noqa
from foodelivery.ext.db import db
from foodelivery.ext.site import models


def init_app(app):
    @app.cli.command()
    def create_db():
        """Database initialization"""
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """Add new user"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        click.echo(f"User {email} created successfully!")

    @app.cli.command()
    def list_orders():
        click.echo("List of orders")

    @app.cli.command()
    def list_users():
        click.echo("List of users")
