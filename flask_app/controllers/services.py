from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, service

@app.route('/book_with_me')
def book():
    if "user_id" not in session:
        return redirect("/dashboard")
    data = {
        'id': session["user_id"]
    }
    print("session", session)
    return render_template("booking.html", user=user.User.get_id(data), service=service.Service.get_all_services())

@app.route("/book_with_me", methods=['POST'])
def create_booking():
    booking_appointment = request.form
    if not service.Service.is_valid(booking_appointment):
        return redirect("/book_with_me")
    if "user_id" not in session:
        return redirect("/")
    data = {
        "cut": request.form["cut"],
        "color": request.form["color"],
        "description": request.form["description"],
        "date": request.form["date"],
        "user_id": session["user_id"]
    }
    service.Service.create_new_service(data)
    return redirect("/confirmation")

@app.route("/confirmation")
def confirm():
    return render_template("confirmation.html")