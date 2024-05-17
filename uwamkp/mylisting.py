from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required
from flask_login import current_user
from uwamkp.models import db
from uwamkp.models import Listing
from sqlalchemy import select


bp = Blueprint('mylisting', __name__, url_prefix='/mylisting')


@bp.route('/listings', methods=["GET"])
@login_required
def my_listing():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('query', '', type=str)
    show_sold = request.args.get('show_sold', 'off', type=str)
    sort_by = request.args.get('sort', 'newest', type=str)

    per_page = 6
    start = (page - 1) * per_page
    end = start + per_page

    stmt = select(
        Listing
    ).where(
        Listing.seller_id == current_user.id
    ).where(
        Listing.deleted == False
    )

    if search_query:
        stmt = stmt.where(Listing.title.ilike(f'%{search_query}%'))

    if sort_by == 'newest':
        stmt = stmt.order_by(Listing.created_at.desc())
    elif sort_by == 'oldest':
        stmt = stmt.order_by(Listing.created_at.asc())

    if show_sold == 'off':
        stmt = stmt.where(Listing.sold == False)

    listings = db.session.scalars(stmt).all()
    listings_dict = [i.to_dict() for i in listings]

    listings_paginated = listings_dict[start:end]
    total_pages = (len(listings) + per_page - 1) // per_page

    return render_template("mylisting.html",
                           listings=listings_paginated,
                           current_user=current_user,
                           page=page,
                           total_pages=total_pages,
                           show_sold=show_sold,
                           query=search_query,
                           sort=sort_by)
