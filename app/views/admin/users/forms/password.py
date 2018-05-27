# -*- coding: utf8 -*-

from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, validators
from flask_babel import lazy_gettext as _lg
from app.models import Role
from app.helpers import get_timezones
import config


class PasswordForm(FlaskForm):
    password = PasswordField(_lg('USER_PASSWORD'), [
        validators.Required(),
        validators.EqualTo('confirm_password', message=_lg('USER_CONFIRM_PASSWORD_INVALID')),
        validators.Length(min=6, max=64)
    ])
    confirm_password = PasswordField(_lg('USER_CONFIRM'), [validators.Optional()])

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
