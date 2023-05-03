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


"""
class WalkForm(FlaskForm):
    fuel = SelectField(
        choices=[('No Fuel', 'No Fuel')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')
    
class BikeForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric'),('No Fuel', 'No Fuel')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class CarForm(FlaskForm):
    fuel = SelectField(
        choices=[
            ('Diesel','Diesel'),
            ('Gas', 'Gas'),
            ('Electric','Electric (BEV)'),
            ('Electric & Gas','Plug-in Hybrid (PHEV)')
        ],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class BusForm(FlaskForm):    
    fuel = SelectField(
        choices=[('Diesel', 'Diesel')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class MotorcycleForm(FlaskForm):
    fuel = SelectField(
        choices=[('Gas', 'Gas')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class TrainForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class TramForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class MetroForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class FerryForm(FlaskForm):
    fuel = SelectField(
        choices=[
            ('With_Car', 'With Car'),
            ('Without_Car', 'Without Car')
        ],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class PlaneForm(FlaskForm):
    fuel = SelectField(
        choices=[('Domestic', 'Jetfuel (Kerosine)')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')
"""
