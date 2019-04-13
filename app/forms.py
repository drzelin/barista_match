from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from wtforms.fields.html5 import EmailField
import phonenumbers


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RequestForm(FlaskForm):
    cafe_name = StringField('Cafe Name', [validators.DataRequired()])
    owner_name = StringField('Owner Name', [validators.DataRequired()])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    phone = StringField('Phone', [validators.DataRequired()])

    def validate_phone(form, field):
        if len(field.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1"+field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
    submit = SubmitField('Submit Request')
