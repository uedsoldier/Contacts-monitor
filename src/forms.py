from flask_wtf import Form
from wtforms import Form, StringField, PasswordField, SubmitField, IntegerField,validators
from wtforms.validators import InputRequired, NumberRange, Length

class LoginForm(Form):
    login_user = StringField('Usuario', id='user-login', validators=[InputRequired('Usuario requerido'),Length(min=2,max=16)])
    login_password = PasswordField('Contraseña', id='password-login', validators=[InputRequired('Contraseña requerida'),Length(min=3,max=32)])
    submit = SubmitField('Acceder', id='submit-login')
