from flask import Flask

from . import auth
from . import listing


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from . import db
    db.init_app(app)

    app.config.from_mapping(
        SECRET_KEY='5505groupprojectYgvfe',
        DATABASE=app.instance_path,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(auth.bp)
    app.register_blueprint(listing.bp)

    return app
