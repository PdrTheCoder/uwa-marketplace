from flask import render_template
from flask import Blueprint


bp = Blueprint('listing', __name__, url_prefix='/listing')


# ======= my listing ===========
@bp.route('/myListing')
def my_listing():
    return render_template("mylisting.html")

# ======= end my listing ===========
@bp.route('/addproduct')
def add_product():
     return render_template("addproduct.html")

# ======= other views 1 ===========
# other
# ======= end other views 1 ===========


# ======= other views 2 ===========
# other
# ======= end other views 2 ===========


# ======= other views 3 ===========
# other
# ======= end other views 3 ===========
