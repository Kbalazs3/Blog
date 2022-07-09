from flask import Blueprint, render_template


auths = Blueprint("auths", __name__)


@auths.route("/login")
def log_in():
    return "log in"


@auths.route("/sign-up")
def sign_up():
    return "sign up"


@auths.route("/log-out")
def log_out():
    return "log out"

