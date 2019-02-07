from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = PasswordField("Password", [validators.Length(min=6, max=144)])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    email = StringField("Email", [validators.Length(min=2, max=144), validators.Email(message=(u'That\'s not a valid email address.'))])
    
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = PasswordField("Password", [validators.Length(min=6, max=144)])
    confirm_password = PasswordField("Confirm password", [validators.Length(min=6, max=144)])

    class Meta:
        csrf = False
