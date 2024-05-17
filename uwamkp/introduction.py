from flask import Flask
from flask import Blueprint
from flask import render_template

bp = Blueprint('introduction', __name__)

@bp.route('/introduction', methods=['GET'])
def intro():
    return render_template("introduction.html")