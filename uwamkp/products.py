from flask import Blueprint
from flask import render_template


bp = Blueprint('addproduct', __name__, url_prefix='/addproduct')


@bp.route('/addproduct', methods=["GET"])
def login():
    return render_template("addproduct.html")


@app.route('/details')
def productdetails():
    return render_template('details.html')
