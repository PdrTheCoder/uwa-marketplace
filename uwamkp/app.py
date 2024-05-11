from flask import Flask
from flask_login import LoginManager
from uwamkp.models import db
from uwamkp.models import User
from flask_migrate import Migrate
from uwamkp.auth import bp as auth_bp
from uwamkp.mylisting import bp as mylisting_bp
from uwamkp.signup import bp as signup_bp
from sqlalchemy import select

import os


# create the app and db
app = Flask(__name__)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///uwamkp.db"
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

db.init_app(app)
migrate = Migrate(app, db)

# init login manager instance
login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(mylisting_bp)
app.register_blueprint(signup_bp)


@login_manager.user_loader
def load_user(user_id):
    stmt = select(User).where(User.id == user_id)
    user = db.session.scalars(stmt).one_or_none()
    return user
