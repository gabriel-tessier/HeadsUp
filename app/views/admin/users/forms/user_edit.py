# -*- coding: utf8 -*-

from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, TextAreaField, PasswordField, SelectField, validators
from flask_babel import lazy_gettext as _lg
from app.models import Role
from app.helpers import get_timezones
import config


class UserEditForm(FlaskForm):
    email = TextField(_lg('USER_EMAIL'), [
        validators.Required(),
        validators.Email(),
        validators.Length(min=10, max=255)
    ])
    name = TextField(_lg('USER_NAME'), [
        validators.Required(),
        validators.Length(min=3, max=255)
    ])
    nickname = TextField(_lg('USER_NICKNAME'), [
        validators.Required(),
        validators.Length(min=0, max=64)
    ])
    role_id = SelectField(_lg('USER_ROLE'), [
        validators.Optional()],
        choices=Role.DEFAULT_USER_ROLES)
    timezone = SelectField(_lg('USER_TIMEZONE'), choices=get_timezones())

    def __init__(self, user=None, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        if not user:
            self.timezone.data = config.DEFAULT_TIMEZONE

        if not self.is_submitted() and user:
            self.email.data = user.email
            self.name.data = user.name
            self.nickname.data = user.nickname
            self.role_id.data = user.role_id
            self.timezone.data = user.timezone
