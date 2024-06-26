from flask import Flask
from flask import redirect
from flask import url_for
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from sqlalchemy import select
from uwamkp.models import db
from uwamkp.models import User
from uwamkp.auth import bp as auth_bp
from uwamkp.mylisting import bp as mylisting_bp
from uwamkp.products import bp as products_bp
from uwamkp.showcase import showcase_bp
from uwamkp.introduction import bp as introduction_bp
from uwamkp.api import bp as api_bp


# create the app and db
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///uwamkp.db"
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["PHOTO_FOLDER"] = 'images'

db.init_app(app)
migrate = Migrate(app, db)

# init login manager instance
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"

app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)
app.register_blueprint(introduction_bp)

# At the begining we split blueprints to avoide possible conflicts.
# TODO suppose to merge below three blueprint into one blueprint.
# need more time to do this carefully, do not end up with a mess.
app.register_blueprint(mylisting_bp)
app.register_blueprint(showcase_bp)
app.register_blueprint(products_bp)


@login_manager.user_loader
def load_user(user_id):
    stmt = select(User).where(User.id == user_id)
    user = db.session.scalars(stmt).one_or_none()
    return user


@app.route("/")
def slash():
    return redirect(url_for("showcase.showcase"))
