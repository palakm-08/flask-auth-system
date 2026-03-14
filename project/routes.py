from project import app, db
from flask import render_template, redirect, url_for, flash
from project.forms import RegisterForm
from project.models import User

@app.route('/')
def home_pg():
    return render_template('home.html')

@app.route('/register')
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(u_id = form.username.data,
                              u_email = form.email_address.data,
                              password_hash = form.password1.data 
                              )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_pg'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user : {err_msg}', category='danger')


@app.route('/login')
def login_page():
    return "Flask is running"