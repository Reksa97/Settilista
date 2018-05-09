from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    # Length of all fields must be between 3 and 144 
    username = StringField("Username", [validators.Length(min=3, max=144)])
    name = StringField("Name", [validators.Length(min=3, max=144)])
    password = PasswordField("Password", [validators.Length(min=3, max=144)])

    class Meta:
        csrf = False