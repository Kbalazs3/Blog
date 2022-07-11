from flask import Blueprint, render_template, redirect, url_for, request


auths = Blueprint("auths", __name__)


@auths.route("/login", methods=["GET", "POST"])
def log_in():
    return render_template("login.html")


@auths.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    sign_up_email = request.form.get("sign_up_email")
    print(sign_up_email)
    return render_template("signup.html")


@auths.route("/log-out")
def log_out():
    return redirect(url_for("views.index"))

