from flask import Blueprint, render_template, redirect, url_for


auths = Blueprint("auths", __name__)


@auths.route("/login")
def log_in():
    return render_template("login.html")


@auths.route("/sign-up")
def sign_up():
    return render_template("signup.html")


@auths.route("/log-out")
def log_out():
    return redirect(url_for("views.index"))

