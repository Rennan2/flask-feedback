"""Forms for flask-feedback."""

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    """form for login"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=4, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=5, max=55)],
    )


class RegisterForm(FlaskForm):
    """user registration"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=4, max=20)],
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
    )
    first_name = StringField(
        "first name", validators=[InputRequired(), Length(max=100)]
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
    )


class FeedbackForm(FlaskForm):
    """feedback form"""

    title = StringField(
        "title",
        validators=[InputRequired(), Length(max=150)],
    )
    content = StringField(
        "content",
        validators=[InputRequired()],
    )


class DeleteForm(FlaskForm):
    """delete form"""

    submit = PasswordField("Confirm")
