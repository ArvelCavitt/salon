from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, service

@app.route('/book_with_me')
def book():
    return render_template("booking.html")