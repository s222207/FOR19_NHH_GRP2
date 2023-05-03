from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange 

class RegForm(FlaskForm):
    transport = SelectField(
        choices=[
            ('Walking', 'Walking'),
            ('Bike', 'Bike'),
            ('Car', 'Car'),
            ('Motorcycle', 'Motorcycle'),
            ('Bus', 'Bus'),
            ('Plane', 'Plane'),
            ('Ferry', 'Ferry'),
            ('Train', 'Train'),
            ('Tram', 'Tram'),
            ('Metro', 'Metro')
        ],
        validators=[DataRequired()]
    )
    fuel = SelectField(
        choices=[
            ('Diesel', 'Diesel'),
            ('Gas', 'Gas'),
            ('Electric', 'Electric (BEV)'),
            ('Electric & Gas', 'Plug-in Hybrid (PHEV)'),
            ('No Fuel', 'No Fuel'),
            ('Diesel', 'Diesel'),
            ('Domestic', 'Jetfuel (Kerosine)'),
            ('Electric', 'Electric'),
            ('With_Car', 'With Car'),
            ('Without_Car', 'Without Car')
        ],
        validators=[DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators=[DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')
