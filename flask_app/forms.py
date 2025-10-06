from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from flask_app.models import User


class RegistrationForm(FlaskForm):
   
    fname = StringField(
        "First name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Last name", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$",
            message="Password must be 8–32 characters, include uppercase, lowercase, number, and special character."
        )
        ],
    )
    confirm= PasswordField(
        "Confirm password", validators=[DataRequired(), EqualTo("password")]
    )
    submit= SubmitField("Sign up")


    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exist, please coose another one.")


    def validate_email(self,email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exist, please coose another one.")



class LoginForm(FlaskForm):
    
    email= StringField("Email", validators=[DataRequired(), Email()])
    password= PasswordField("Password", validators=[DataRequired()])
    remember=BooleanField("Remember Me")
    submit=SubmitField("Log In")