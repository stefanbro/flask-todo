from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators

class LoginForm(Form):
	username = StringField('username', [validators.DataRequired()])
	password = PasswordField('password', [validators.DataRequired()])

class RegisterForm(Form):
	username = StringField('username', [validators.Length(min=1, max=25)])
	email = StringField('email', [validators.Length(min=6, max=64)])
	password = PasswordField('password', [validators.Length(min=6, max=40)])
	password_again = PasswordField('password_again')