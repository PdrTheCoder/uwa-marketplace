from flask import Blueprint
from flask import render_template


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=["GET"])
def login():
    return render_template("login.html")
