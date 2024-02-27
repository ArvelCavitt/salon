from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
from flask_app.models.user import User
from flask_app.models import service
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def log():
    return render_template('log.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    print("session", session)
    return render_template('dashboard.html', user = user.User.get_id(data), all_services = service.Service.get_all_services()) #changing all_services & get_all_services to take in only logged in users services later.#


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login' , methods=['POST'])
def login():
    user_login_data = {
        "email": request.form['email'],
        "password": request.form['password'],
    }
    user_exists = user.User.get_email(user_login_data)
    if not user.User.validate_login(user_exists, user_login_data):
        return redirect('/')
    session['id'] = user_exists['first_name']
    session['first_name'] = user_exists['first_name']
    return redirect('/dashboard')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     user = User.get_email(request.form)
#     if not user:
#         flash("Invalid email", "login")
#         return redirect('/')
#     if bcrypt.check_password_hash(user.password, request.form['password']):
#         flash("Invalid password", "login")
#         return redirect('/')
#     session['user_id'] = user.id
#     return redirect('/dashboard')

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
        "phone": request.form['phone'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = user.User.new_user(data)
    session['user_id'] = id
    return redirect('/dashboard')
