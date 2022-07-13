from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .modules import User

auths = Blueprint("auths", __name__)


@auths.route("/login", methods=["GET", "POST"])
def log_in():
    login_email = request.form.get("email")
    login_password = request.form.get("password")
    return render_template("login.html")


@auths.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        # User sign up sent form data:
        sign_up_email = request.form.get("sign_up_email")
        sign_up_username = request.form.get("username")
        sign_up_password_first = request.form.get("sign_up_password")
        sign_up_pw_again = request.form.get("second_password")
        # Check if user exist, and password is appropriate:
        email_exist = User.query.filter_by(email=sign_up_email).first()
        username_exist = User.query.filter_by(username=sign_up_username).first()
        if email_exist:
            flash('This email address is already registered!', category='error')
        elif username_exist:
            flash('This username is already used!', category='error')
        elif len(sign_up_username) < 2:
            flash('Username is too short! Minimum 2 characters please!', category='error')
        elif sign_up_password_first != sign_up_pw_again:
            flash("Passwords don't match!", category='error')
        elif len(sign_up_password_first) > 6 and



def password_checker(sign_up_pw):
    special_chars = ['$', '@', '#', '%']
    is_pw_valid = True

    if len(sign_up_pw) < 6:
        is_pw_valid = False
    if len(sign_up_pw) > 20:
        is_pw_valid = False
    if not any(char.isdigit() for char in sign_up_pw):
        is_pw_valid = False
    if not any(char.isupper() for char in sign_up_pw):
        is_pw_valid = False
    if not any(char.islower() for char in sign_up_pw):
        is_pw_valid = False
    if not any(char in special_chars for char in sign_up_pw):
        is_pw_valid = False

    return is_pw_valid


password_checker(sign_up_pw="test")

@auths.route("/log-out")
def log_out():
    return redirect(url_for("views.index"))

