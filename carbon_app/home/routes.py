from flask import render_template, Blueprint
from carbon_app.models import User, Transport
home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_func():
    return render_template('home.html')
