from flask import Flask
from flask import redirect
from flask_login import LoginManager
from flask_login import current_user
from flask_migrate import Migrate
import os
from sqlalchemy import select
from uwamkp.models import db
from uwamkp.models import User
from uwamkp.auth import bp as auth_bp
from uwamkp.mylisting import bp as mylisting_bp
from uwamkp.constants import INDEX_LOGGED
from uwamkp.constants import INDEX_ANONYMOUS


# create the app and db
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


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



@login_manager.user_loader
def load_user(user_id):
    stmt = select(User).where(User.id == user_id)
    user = db.session.scalars(stmt).one_or_none()
    return user


@app.route("/")
def slash():
    if current_user.is_authenticated:
        return redirect(INDEX_LOGGED)
    else:
        return redirect(INDEX_ANONYMOUS)
