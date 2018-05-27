# -*- coding: utf8 -*-

from flask_wtf import FlaskForm
from wtforms import BooleanField, validators
from flask_babel import lazy_gettext as _lg
from app.models import Role
from app.helpers import get_timezones
import config


class UserEmailNotificationForm(FlaskForm):
    allow_digest = BooleanField([validators.Optional()])
    allow_comment = BooleanField([validators.Optional()])

    def __init__(self, user=None, *args, **kwargs):
        super(UserEmailNotificationForm, self).__init__(*args, **kwargs)

        if not user:
            self.timezone.data = config.DEFAULT_TIMEZONE

        if not self.is_submitted() and user:
            self.allow_digest.data = user.allow_digest
            self.allow_comment.data = user.allow_comment
