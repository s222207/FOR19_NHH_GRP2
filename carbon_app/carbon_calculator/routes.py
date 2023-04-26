from flask import render_template, Blueprint, redirect, url_for, flash
from carbon_app.models import Transport, db
from carbon_app.carbon_calculator.form import WalkForm, BikeForm, CarForm, BusForm, MotorcycleForm, MetroForm, TrainForm, TramForm, FerryForm, PlaneForm
from flask_login import login_required, current_user
from datetime import datetime, timedelta
import json

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
co2eqIDX['Bike']= {'Electric':0.2, 'No Fuel':0}
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
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
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = Transport(kms=kms, fuel=fuel, transport=transport,total=total, author=current_user, )
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_calculator.your_data'))
    return render_template('carbon_calculator/NE/new_entry_plane.html', title='New Entry', form=form)

@carbon_calculator.route('/carbon_calculator/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    
    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(Transport.total), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        emission_transport[0]=first_tuple_elements[index_walk]
    else:
        emission_transport[0]

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[1]=first_tuple_elements[index_bus]
    else:
        emission_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        emission_transport[2]=first_tuple_elements[index_car]
    else:
        emission_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        emission_transport[3]=first_tuple_elements[index_ferry]
    else:
        emission_transport[3]

    if 'Motorcycle' in second_tuple_elements:
        index_motorcycle = second_tuple_elements.index('Motorcycle')
        emission_transport[4]=first_tuple_elements[index_motorcycle]
    else:
        emission_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[5]=first_tuple_elements[index_plane]
    else:
        emission_transport[5]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[6]=first_tuple_elements[index_train]
    else:
        emission_transport[6]

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        emission_transport[7]=first_tuple_elements[index_tram]
    else:
        emission_transport[7]

    if 'Metro' in second_tuple_elements:
        index_metro = second_tuple_elements.index('Metro')
        emission_transport[8]=first_tuple_elements[index_metro]
    else:
        emission_transport[8]
  
    if 'Bike' in second_tuple_elements:
        index_bike = second_tuple_elements.index('Bike')
        emission_transport[9]=first_tuple_elements[index_bike]
    else:
        emission_transport[9]

    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(Transport.kms), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[0]=first_tuple_elements[index_walk]
    else:
        kms_transport[0] 

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[1]=first_tuple_elements[index_bus]
    else:
        kms_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[2]=first_tuple_elements[index_car]
    else:
        kms_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[3]=first_tuple_elements[index_ferry]
    else:
        kms_transport[3]

    if 'Motorcycle' in second_tuple_elements:
        index_motorcycle = second_tuple_elements.index('Motorcycle')
        kms_transport[4]=first_tuple_elements[index_motorcycle]
    else:
        kms_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[5]=first_tuple_elements[index_plane]
    else:
        kms_transport[5]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[6]=first_tuple_elements[index_train]
    else:
        kms_transport[6]     

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        kms_transport[7]=first_tuple_elements[index_tram]
    else:
        kms_transport[7]   

    if 'Metro' in second_tuple_elements:
        index_metro = second_tuple_elements.index('Metro')
        kms_transport[8]=first_tuple_elements[index_metro]
    else:
        kms_transport[8]
    
    if 'Bike' in second_tuple_elements:
        index_bike = second_tuple_elements.index('Bike')
        kms_transport[9]=first_tuple_elements[index_bike]
    else:
        kms_transport[9]

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(Transport.total), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      


    return render_template('carbon_calculator/carbon_calculator.html', title='your_data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

#Delete emission
@carbon_calculator.route('/carbon_calculator/delete_emissions/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry Deleted", "success")
    return redirect(url_for('carbon_calculator.your_data'))
    
