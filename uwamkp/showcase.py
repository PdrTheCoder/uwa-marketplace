from flask import Blueprint, render_template, request, jsonify
from uwamkp.models import Listing, db
from sqlalchemy import select
from flask_login import current_user

showcase_bp = Blueprint('showcase', __name__, url_prefix='/showcase')


@showcase_bp.route('/')
def showcase():
    page = request.args.get('page', 1, type=int)
    per_page = 12
    search_query = request.args.get('query', '', type=str)
    sort_by = request.args.get('sort', 'newest', type=str)

    try:
        stmt = select(Listing).where(Listing.deleted == False).where(Listing.sold == False)

        if search_query:
            stmt = stmt.where(Listing.title.ilike(f'%{search_query}%'))

        if sort_by == 'newest':
            stmt = stmt.order_by(Listing.created_at.desc())
        elif sort_by == 'oldest':
            stmt = stmt.order_by(Listing.created_at.asc())
        elif sort_by == 'price_low_high':
            stmt = stmt.order_by(Listing.price.asc())
        elif sort_by == 'price_high_low':
            stmt = stmt.order_by(Listing.price.desc())

        listings = db.session.scalars(stmt).all()
    except Exception as e:
        print(f"Error querying listings: {e}")
        return "An error occurred while querying listings", 500

    total = len(listings)
    start = (page - 1) * per_page
    end = start + per_page
    listings_paginated = listings[start:end]

    try:
        listings_dict = [listing.to_dict() for listing in listings_paginated]
    except Exception as e:
        print(f"Error converting listings to dict: {e}")
        listings_dict = []

    total_pages = (total + per_page - 1) // per_page

    try:
        return render_template('showcase.html', listings=listings_dict, page=page, total_pages=total_pages, query=search_query, sort=sort_by)
    except Exception as e:
        print(f"Error rendering template: {e}")
        return "An error occurred while rendering the template", 500


@showcase_bp.route('/is_logged_in')
def is_logged_in():
    return jsonify(logged_in=current_user.is_authenticated)
