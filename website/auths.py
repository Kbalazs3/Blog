from flask import Blueprint


auths = Blueprint("auths", __name__)


@auths.route("/login")
def log_in():
    return "INDEX"