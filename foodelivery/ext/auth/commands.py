import click # noqa
from foodelivery.ext.db import db
from foodelivery.ext.auth.models import User


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """Add new user"""
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()
    click.echo(f"User {email} created successfully!")


def list_users():
    users = User.query.all()
    click.echo(f'Users list: {users}')
