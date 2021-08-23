from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Enter Username:',validators=[Required()])
    password = PasswordField('Enter Password:',validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegForm(FlaskForm):
    email = StringField('Enter Your Email Address:', validators=[Required(),Email()])
    username = StringField('Enter Your Username:', validators=[Required()])
    password = PasswordField('Enter Your Password:',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password Entered:',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email address taken")
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("Username taken")