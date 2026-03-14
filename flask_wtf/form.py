from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField, SubmitField
from wtforms.validators import DataRequired ,Email,Length

class RegistrationForm(FlaskForm):
    name = StringField("Full name",validators=[DataRequired(message = "we need your name , it cannot be empty")])
    email = StringField("Email", validators=[DataRequired(message =" email message is required "), Email(message="that doesn't look like a valid email")])
    password = PasswordField("Password",validators=[DataRequired(message="password required "),Length(min=6 ,message="password must be 6 character ")])
    submit = SubmitField("Register")
