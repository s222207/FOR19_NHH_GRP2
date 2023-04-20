from flask import render_template, Blueprint, redirect, url_for, flash
from carbon_app.models import Transport, db
from carbon_app.carbon_calculator.form import WalkForm, BikeForm, CarForm, BusForm, MotorcycleForm, MetroForm, TrainForm, TramForm, FerryForm, PlaneForm
from flask_login import login_required, current_user
from datetime import datetime, timedelta

carbon_calculator=Blueprint('carbon_calculator',__name__)

@carbon_calculator.route('/carbon_calculator')
def carbon_calculator_func():
    return render_template('carbon_calculator/carbon_calculator.html', title='Calculator')

@carbon_calculator.route('/carbon_calculator/new_entry', methods=['GET','POST'])
@login_required
def new_entry():
    return render_template('carbon_calculator/new_entry.html', title='New Entry', condition = 'T')

#New Entries

#Dictionaries - emission factors:
co2eqIDX={}
co2eqIDX['Car'] = {'Diesel':141.8, 'Gas':155.5, 'Electric & Gas':88.4, 'Electric':7.3}
co2eqIDX['Bike']= {'No Fuel':0, 'Electric':0.2}
co2eqIDX['Walk']= {'No Fuel':0}
co2eqIDX['Bus'] = {'Diesel':93.8}
co2eqIDX['Motorcycle']={'Gas':163.5}
co2eqIDX['Metro']={'Electric':3.9}
co2eqIDX['Tram']= {'Electric':3.1}
co2eqIDX['Train']={'Electric':0.4}
co2eqIDX['Ferry']={'With_Car':1063.9, 'Without_Car':54.1}
co2eqIDX['Plane']={'Domestic':101}

@carbon_calculator.route('/carbon_calculator/NE/new_entry_bike.html', methods=['GET','POST'])
@login_required
def new_entry_bike():
    form = BikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Bike'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_bike.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_walk.html', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Walk'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_walk.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_bus.html', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Bus'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_bus.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_car.html', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Car'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_car.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_motorcycle.html', methods=['GET','POST'])
@login_required
def new_entry_motorcycle():
    form = MotorcycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Motorcycle'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_motorcycle.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_train.html', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Train'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_train.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_ferry.html', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Ferry'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_ferry.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_tram.html', methods=['GET','POST'])
@login_required
def new_entry_tram():
    form = TramForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Tram'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_tram.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_metro.html', methods=['GET','POST'])
@login_required
def new_entry_metro():
    form = MetroForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Metro'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_metro.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/NE/new_entry_plane.html', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = 'Plane'
        co2eq = float(kms)*co2eqIDX[transport][fuel]
        co2eq = round(co2eq,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,co2eq=co2eq, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_plane.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/your_data')
@login_required
def your_data():
    entries = Transport.query.filter_by(author=current_user).\
    filter(Transport.date>(datetime.now()-timedelta(days=5))).\
    order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()

    return render_template('carbon_calculator/your_data.html', title='Your Data', entries=entries)

@carbon_calculator.route('/carbon_calculator/delete_emissions/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry Deleted", "success")
    return redirect(url_for('carbon_calculator.your_data'))
