from flask import render_template, Blueprint, redirect, flash, url_for, request
from carbon_app.users.forms import RegistrationForm, LoginForm

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Your account has been created! Login to use our app.', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  error = None
  if request.method == 'POST':
    if request.form['email'] != 'aa@demo.com':
      error = 'No user registered with that email. Please register or try again.'
    else:
      if request.form['email'] == 'aa@demo.com' and request.form['password'] != '111':
        error = 'Wrong password. Please try again.'
      else:
        return redirect(url_for('home.home_func'))

  return render_template('users/login.html', title='login', form=form, error=error)