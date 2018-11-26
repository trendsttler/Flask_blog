from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtFforms.validators import DataRequired, Length, Email, EqualTo

class ResgistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    
    password = PasswordField('password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('SignUp')


class LoginForm(FlaskForm):
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    
    password = PasswordField('password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('LogIn')