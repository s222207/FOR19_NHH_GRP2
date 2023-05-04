from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from carbon_app.models import User

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators = [DataRequired(), Length(min=2, max=30)]
    )
    email = StringField(
        'Email',
        validators = [DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators = [DataRequired(), Length(min=8, max=30)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators = [DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

#Validate username and email
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one.')
        
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('A user is already registered with that email. Please log in or choose a different one.')    

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators = [DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators = [DataRequired()]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
