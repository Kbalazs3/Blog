from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
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
        is_pw_valid = password_checker(sign_up_password_first)
        is_email_valid = sign_up_email_checker(sign_up_email)
        sign_up_pw_again = request.form.get("second_password")
        # Check if user exist, and password is appropriate:
        email_exist = User.query.filter_by(email=sign_up_email).first()
        username_exist = User.query.filter_by(username=sign_up_username).first()
        if email_exist:
            flash('This email address is already registered!', category='error')
        elif not is_email_valid:
            flash('The given e-mail adress is not correct!', category='error')
        elif username_exist:
            flash('This username is already used!', category='error')
        elif len(sign_up_username) < 2:
            flash('Username is too short! Minimum 2 characters please!', category='error')
        elif sign_up_password_first != sign_up_pw_again:
            flash("Passwords don't match!", category='error')
        elif not is_pw_valid:
            flash('Password not correct!\nRequirements:\n\t - Min 6, max 20 characters\n\t - Min 1 spec. character\n\t - min 1 lowercase and min 1 uppercase letter\n\t - Min 1 digit', category='error')
        else:
            new_user = User(email=sign_up_email, username=sign_up_username, password=sign_up_pw_again)
            db.session.add(new_user)
            db.session.commit()
            flash('User account created!')
            return redirect(url_for("views.index"))


def password_checker(sign_up_pw):
    special_chars = ['$', '@', '#', '%', ',', '.', ':', '_', '-', '*', ';', '?']
    is_pw_valid = True

    if len(sign_up_pw) < 6:
        is_pw_valid = False
        print("Too short pw! Please min 6 characters")
    if len(sign_up_pw) > 20:
        is_pw_valid = False
        print("too long pw, max 20 chars")
    if not any(char.isdigit() for char in sign_up_pw):
        is_pw_valid = False
        print("It has to contain min one digit!")
    if not any(char.isupper() for char in sign_up_pw):
        is_pw_valid = False
        print("min one uppercase letter!")
    if not any(char.islower() for char in sign_up_pw):
        is_pw_valid = False
        print("min 1 lowercase please!")
    if not any(char in special_chars for char in sign_up_pw):
        is_pw_valid = False
        print("please min 1 spec. char!")

    return is_pw_valid


def sign_up_email_checker(sign_up_email):
    is_email_valid = True

    if len(sign_up_email) < 6:
        is_email_valid = False

    email_split = sign_up_email.split('@')

    if len(email_split[0]) < 2:
        is_email_valid = False

    return is_email_valid


@auths.route("/log-out")
def log_out():
    return redirect(url_for("views.index"))

