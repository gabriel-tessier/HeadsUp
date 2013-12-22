from flask.ext.wtf import Form
from wtforms import TextAreaField, TextField, FileField, BooleanField, validators

class CommentForm(Form):
	body = TextAreaField('Body', [ validators.Required() ])