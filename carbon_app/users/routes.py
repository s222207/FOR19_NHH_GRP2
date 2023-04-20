from flask import render_template, Blueprint, redirect, flash, url_for, request
from carbon_app import db, bcrypt
from carbon_app.users.forms import RegistrationForm, LoginForm
from carbon_app.models import User
from flask_login import login_user, current_user, logout_user

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Login to use our app.', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
     return redirect(url_for('home.home_func'))
  error = None
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data) :
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home.home_func'))
    else:
      error = 'Wrong Credentials. Please try again.'

  return render_template('users/login.html', title='Login', form=form, error=error)

@users.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home.home_func'))
