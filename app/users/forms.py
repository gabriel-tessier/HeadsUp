from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, TextAreaField, PasswordField, SelectField, validators
from flask.ext.babel import lazy_gettext, gettext

class UserForm(Form):
	email = TextField(lazy_gettext('Email'), [ validators.Required(), validators.Email() , validators.Length(min = 10, max = 255)])
	name = TextField(lazy_gettext('Name'), [ validators.Required(), validators.Length(min = 5, max = 255) ])
	nickname = TextField(lazy_gettext('Nickname'), [ validators.Required() , validators.Length(min = 0, max = 64)])
	role = SelectField(lazy_gettext('Role'), [validators.Optional()], choices=[('1','Administrator'),('2','Writer')])
	password = PasswordField(lazy_gettext('Password'), [ 
		validators.Optional(), 
		validators.EqualTo('confirm_password', message=lazy_gettext('Please repeat the password')),
		validators.Length(min = 6, max = 64)
	])
	confirm_password = PasswordField(lazy_gettext('Confirm'), [ validators.Optional() ])
	address = TextAreaField(lazy_gettext('Address'), [ validators.Length(min = 0, max = 255) ])
	phone = TextField(lazy_gettext('Phone'), [ validators.Length(min = 0, max = 64) ])

class NewUserForm(UserForm):
	password = PasswordField(lazy_gettext('Password'), [ 
		validators.Required(), 
		validators.EqualTo('confirm_password', message=lazy_gettext('Please repeat the password')),
		validators.Length(min = 6, max = 64)
	])

class EditUserForm(UserForm):

	def __init__(self, user, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.email.data = user.email
		self.name.data = user.name
		self.nickname.data = user.nickname
		self.role.data = unicode(user.role)
		self.address.data = user.address
		self.phone.data = user.phone



