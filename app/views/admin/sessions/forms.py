# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, PasswordField, validators
from flask_babel import lazy_gettext as _lg, gettext as _
from app.models import User


class LoginForm(FlaskForm):
    email = TextField(_lg('USER_EMAIL'), [validators.Email(), validators.Length(min=10, max=255)])
    password = PasswordField(_lg('USER_PASSWORD'), [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)


class SignUpForm(FlaskForm):
    email = TextField(_lg('USER_EMAIL'), [validators.Email(), validators.Length(min=10, max=255)])
    name = TextField(_lg('USER_NAME'), [validators.Required()])
    nickname = TextField(_lg('USER_NICKNAME'), [validators.Required()])
    password = PasswordField(_lg('USER_PASSWORD'), [validators.Required(), validators.Length(min=10, max=64)])
    check_tos = BooleanField('check_tos', default=False)

    def validate(self):
        valid = super(SignUpForm, self).validate()

        if self.name.data != User.make_valid_name(self.name.data):
            self.name.errors.append(_('USER_NAME_INVALID'))
            valid = False

        if self.nickname.data != User.make_valid_nickname(self.nickname.data):
            self.nickname.errors.append(_('USER_NICKNAME_INVALID'))
            valid = False

        if User.is_email_taken(self.email.data):
            self.email.errors.append(_('USER_EMAIL_TAKEN_ERROR'))
            valid = False

        if User.is_nickname_taken(self.nickname.data):
            self.nickname.errors.append(_('USER_NICKNAME_TAKEN_ERROR'))
            valid = False

        return valid
