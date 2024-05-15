from flask import Blueprint, render_template, request
from uwamkp.models import Listing
from sqlalchemy import select
from uwamkp.models import db

showcase_bp = Blueprint('showcase', __name__, url_prefix='/showcase')

@showcase_bp.route('/')
def showcase():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 12
        stmt = select(Listing).where(Listing.deleted == False).order_by(Listing.created_at.desc())
        listings = db.session.scalars(stmt).all()
        
        # Implementing pagination manually
        total = len(listings)
        start = (page - 1) * per_page
        end = start + per_page
        listings_paginated = listings[start:end]
        listings_dict = [listing.to_dict() for listing in listings_paginated]

        # Calculate total pages
        total_pages = (total + per_page - 1) // per_page

        return render_template('Showcase.html', listings=listings_dict, page=page, total_pages=total_pages)
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred", 500
