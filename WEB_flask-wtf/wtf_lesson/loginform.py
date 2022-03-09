from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])

    username_cap = StringField('капитана', validators=[DataRequired()])
    password_cap = PasswordField(
        'Пароль капитана', validators=[DataRequired()])

    submit = SubmitField('Доступ')
