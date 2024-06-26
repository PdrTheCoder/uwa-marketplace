# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from wtforms import ValidationError
from uwamkp.models import User


class LoginForm(FlaskForm):
    """
    Here we only validate they are empty. Because most of the validations
    are done during registration.
    """
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # TODO remember_me = BooleanField('Keep me logged in')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email(),
                                             Regexp(r'^\d{8}@student\.uwa\.edu\.au$', 0, 'Email must be 8 digits followed by @student.uwa.edu.au')
                                             ])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Username must start with a letter and include only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.'),
        Length(min=8, message='Password must be at least 8 characters long.'),
        Regexp('(?=.*[a-z])', 0, 'Password must contain at least one lowercase letter.'),
        Regexp('(?=.*[A-Z])', 0, 'Password must contain at least one uppercase letter.'),
        Regexp('(?=.*[0-9])', 0, 'Password must contain at least one digit.'),
        Regexp('(?=.*[!@#$%^&*(),.?":{}|<>])', 0, 'Password must contain at least one special character from the set: !@#$%^&*(),.?":{}|<>.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.') 
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
