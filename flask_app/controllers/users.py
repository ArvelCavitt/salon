from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def log():
    return render_template('log.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = user.User.get_email(request.form)
    if not user:
        flash("Invalid email", "login")
        return redirect('/')
    if bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/register', methods = ['POST'])
def register():
    if not user.User.validate_register(request.form):
        return redirect('/register')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = user.User.new_user(data)
    session['user_id'] = id
    return redirect('/dashboard')