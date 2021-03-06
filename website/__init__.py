from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

#from .views import views
#from .auths import auths

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Ruby"
    app.config["SQL_ALCHEMY_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auths import auths

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auths, url_prefix="/")
    from .modules import User
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("/website" + DB_NAME):
        db.create_all(app=app)
        print("Create Database!")
