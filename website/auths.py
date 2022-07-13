from flask import Blueprint, render_template, redirect, url_for, request


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
        sign_up_email = request.form.get("sign_up_email")
        sign_up_username = request.form.get("username")
        sign_up_password_first = request.form.get("sign_up_password")
        sign_up_pw_again = request.form.get("second_password")


@auths.route("/log-out")
def log_out():
    return redirect(url_for("views.index"))

