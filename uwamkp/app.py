from flask import Flask
from uwamkp.models import db
from flask_migrate import Migrate
from uwamkp.auth import bp as auth_bp
from uwamkp.mylisting import bp as mylisting_bp
from uwamkp.products import bp as products_bp
from flask import render_template

# create the app and db
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///uwamkp.db"
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(mylisting_bp)
app.register_blueprint(products_bp)
