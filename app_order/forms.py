from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    shipping_address = StringField('Adres do wysyłki', validators=[DataRequired()])
    product = StringField('Produkt', validators=[DataRequired()])
    submit = SubmitField('Złóż zamówienie')
