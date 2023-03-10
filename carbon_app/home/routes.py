from flask import render_template, Blueprint
home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_func():
    return render_template('home.html')