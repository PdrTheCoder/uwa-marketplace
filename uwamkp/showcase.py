from flask import Blueprint, render_template

showcase_bp = Blueprint('showcase', __name__, url_prefix='/showcase')

@showcase_bp.route('/')
def showcase():
    return render_template('Showcase.html')
