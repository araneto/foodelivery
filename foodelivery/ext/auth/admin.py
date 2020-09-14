from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from foodelivery.ext.auth.models import User
from foodelivery.ext.db import db
from flask import flash


class UserAdmin(ModelView):
    """return None"""
    column_formatters = {
        "email": lambda s, r, u, *a: u.email.split("@")[0]
    }
    column_list = ["email", "admin"]
    can_edit = False
    can_create = True
    can_delete = True
    column_searchable_list = ["email"]
    column_filters = ["email", "admin"]

    @action(
        'toggle_admin',
        'Toggle admin status',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f" {len(users)} user(s) changed successfully", "success")
