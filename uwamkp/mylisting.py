from flask import Blueprint
from flask import render_template
from flask import flash
from uwamkp.models import db
from uwamkp.models import Listing
from sqlalchemy import select

from flask import jsonify


bp = Blueprint('mylisting', __name__, url_prefix='/mylisting')


@bp.route('/listings', methods=["GET"])
def my_listing():
    # TODO get current user id
    # TODO maybe pagination later, maybe not
    stmt = select(Listing).where(Listing.seller_id == 1)
    listings = db.session.scalars(stmt).all()
    listings_dict = [i.to_dict() for i in listings]
    return render_template("mylisting.html", listings=listings_dict)


@bp.route('/listings/<listing_id>', methods=["DELETE"])
def delete_listing(listing_id):
    # TODO first check if the user is admin - need flask-login ready
    # TODO check if the listing is belong to current user - need flask-login ready
    stmt = select(Listing).where(Listing.id == listing_id)
    listing = db.session.scalars(stmt).one_or_none()

    msg = "error"
    code = -1
    category = 'danger'

    if listing:
        try:
            db.session.delete(listing)
            db.session.commit()
            msg = 'Successfully delete the listing.'
            code = 0
            category = 'success'
        except Exception as e:
            # TODO use log later
            msg = f"Delete listing - id: {listing_id} faild."
    else:
        msg = 'Can not find the listing, please try again later.'
    flash(msg, category)
    return jsonify({"msg": msg, "code": code})
