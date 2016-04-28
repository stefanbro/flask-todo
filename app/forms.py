from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = BooleanField('remember_me', validators=[DataRequired()])
