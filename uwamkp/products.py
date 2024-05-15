from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from uwamkp.models import db
from uwamkp.models import Listing

bp = Blueprint('product', __name__)

# todo:login required


@bp.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    # username = current_user.username
    # email = current_user.email
    # created_at = current_user.created_at.isoformat(sep=" ", timespec="seconds")

    if request.method == 'POST':
        title = request.form.get('productTitle')
        price = request.form.get('productPrice')
        condition = request.form.get('productCondition')
        description = request.form.get('productDescription')

        try:
            new_listing = Listing(title=title,
                                  price=float(price),
                                  condition=condition,
                                  description=description
                                  )
            db.session.add(new_listing)
            db.session.commit()
            flash('Your product has been added!')
            return redirect(url_for('details', id=new_listing.id))
        except Exception as e:
            db.session.rollback()
            flash('Error adding product.')
            return render_template("addproduct.html")
    return render_template("addproduct.html")


@bp.route('/details/<int:listing_id>', methods=['GET', 'POST'])
def details(listing_id):
    listing = db.session.query(Listing).get(listing_id)
    return render_template('details.html', listing=listing.to_dict())

# @bp.route('/details/<int:id>',methods=['GET','POST'])
# def details(id):
#     product = Listing.query.get(id)
#     return render_template('details.html')
