from foodelivery.ext.auth import models
from foodelivery.ext.auth.commands import add_user
from foodelivery.ext.auth.commands import list_users
from foodelivery.ext.db import db
from foodelivery.ext.auth.admin import UserAdmin
from foodelivery.ext.admin import admin
from foodelivery.ext.auth.models import User


def init_app(app):
    app.cli.command()(list_users)
    app.cli.command()(add_user)
    admin.add_view(UserAdmin(User, db.session))

