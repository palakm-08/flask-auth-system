from project import app, db
from flask import render_template, redirect, url_for, flash
from project.forms import RegisterForm, LoginForm
from project.models import User

@app.route('/')
def home_pg():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(u_name = form.username.data,
                              u_email = form.email_address.data 
                              )
        user_to_create.set_password(form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_pg'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user : {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        user_in_db = User.query.filter_by(u_name=form.username.data).first()

        if user_in_db and user_in_db.check_password(form.password.data):
            flash(f'Welcome {user_in_db.u_name}!', category='success')
            return redirect(url_for('home_pg'))
        else:
            flash('Invalid username or password!', category='danger')

    return render_template('login.html', form=form)