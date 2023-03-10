from flask import render_template, Blueprint

carbon_calculator=Blueprint('carbon_calculator',__name__)

@carbon_calculator.route('/carbon_calculator')
def carbon_calculator_func():
    return render_template('carbon_calculator/carbon_calculator.html', title='carbon_calculator')

@carbon_calculator.route('/carbon_calculator/new_entry')
def new_entry():
    return render_template('carbon_calculator/new_entry.html',title='new_entry')

@carbon_calculator.route('/carbon_calculator/your_data')
def your_data():
    return render_template('carbon_calculator/your_data.html', title='your_data')