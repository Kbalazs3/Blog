from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path
from .views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = "Ruby"

    app.register_blueprint(views, url_prefix="/")

    return app
