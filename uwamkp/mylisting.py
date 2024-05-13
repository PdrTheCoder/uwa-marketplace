from datetime import datetime
from datetime import timezone
from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask_login import login_required
from flask_login import current_user
from uwamkp.models import db
from uwamkp.models import Listing
from sqlalchemy import select

from flask import jsonify


bp = Blueprint('mylisting', __name__, url_prefix='/mylisting')


@bp.route('/listings', methods=["GET"])
@login_required
def my_listing():
    # handle user profile
    username = current_user.username
    email = current_user.email
    created_at = current_user.created_at.isoformat(sep=" ", timespec="seconds")
    # TODO maybe pagination later, maybe not

    stmt = select(
        Listing
    ).where(
        Listing.seller_id == current_user.id
    ).where(
        Listing.deleted == False
    ).order_by(
        Listing.created_at.desc()
    )

    listings = db.session.scalars(stmt).all()
    listings_dict = [i.to_dict() for i in listings]
    return render_template("mylisting.html",
                           listings=listings_dict,
                           username=username,
                           email=email,
                           created_at=created_at)


@bp.route('/listings/<listing_id>', methods=["PATCH"])
@login_required
def update_listing(listing_id):
    msg = "error"
    code = -1
    category = 'danger'
    updated = False

    stmt = select(Listing).where(Listing.id == listing_id)
    listing = db.session.scalars(stmt).one_or_none()

    if not listing:
        msg = 'Can not find the listing, please try again later.'
        flash(msg, category)
        return jsonify({"msg": msg, "code": code})

    if not current_user.is_admin and listing.seller_id != current_user.id:
        msg = "Deleting this listing is not allowed for this user."
        flash(msg, category)
        return jsonify({"msg": msg, "code": code})

    req_params = request.get_json()
    new_title = req_params.get('title')
    new_condition = req_params.get('condition')
    new_price = req_params.get('price')
    new_description = req_params.get('description')
    new_sold = req_params.get('sold')
    new_deleted = req_params.get('deleted')

    if new_title:
        # TODO validate title
        listing.title = new_title
        updated = True

    if new_condition:
        # TODO validate condition
        listing.condition = new_condition
        updated = True

    if new_price:
        # TODO validate price
        listing.price = new_price
        updated = True

    if new_description:
        # TODO validate new_description
        listing.description = new_description
        updated = True

    if new_sold:
        # TODO validate new sold
        listing.sold = new_sold
        updated = True

    if new_deleted:
        # TODO validate new deleted
        listing.deleted = new_deleted
        updated = True

    if updated:
        listing.updated_at = datetime.now(timezone.utc)
        try:
            db.session.commit()
            msg = 'Successfully updated the listing.'
            code = 0
            category = 'success'
        except exception as e:
            msg = 'Failed to process the request, please try again later.'

    flash(msg, category)
    return jsonify({"msg": msg, "code": code})
