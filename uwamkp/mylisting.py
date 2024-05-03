from flask import Blueprint
from flask import render_template


bp = Blueprint('mylisting', __name__, url_prefix='/mylisting')


@bp.route('/mylisting', methods=["GET"])
def login():
    return render_template("mylisting.html")
