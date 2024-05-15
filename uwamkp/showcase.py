from flask import Blueprint, render_template, request
from uwamkp.models import Listing
from sqlalchemy import select, or_
from uwamkp.models import db

showcase_bp = Blueprint('showcase', __name__, url_prefix='/showcase')

@showcase_bp.route('/')
def showcase():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 12
        search_query = request.args.get('query', '', type=str)
        sort_by = request.args.get('sort', 'newest', type=str)
        
        print(f"Received request with query: {search_query}, sort: {sort_by}, page: {page}")

        stmt = select(Listing).where(Listing.deleted == False)

        if search_query:
            stmt = stmt.where(or_(
                Listing.title.ilike(f'%{search_query}%')
            ))

        if sort_by == 'newest':
            stmt = stmt.order_by(Listing.created_at.desc())
        elif sort_by == 'oldest':
            stmt = stmt.order_by(Listing.created_at.asc())
        elif sort_by == 'price_low_high':
            stmt = stmt.order_by(Listing.price.asc())
        elif sort_by == 'price_high_low':
            stmt = stmt.order_by(Listing.price.desc())

        listings = db.session.scalars(stmt).all()
        
        total = len(listings)
        start = (page - 1) * per_page
        end = start + per_page
        listings_paginated = listings[start:end]
        listings_dict = [listing.to_dict() for listing in listings_paginated]

        total_pages = (total + per_page - 1) // per_page

        print(f"Total listings found: {total}, total pages: {total_pages}")

        return render_template('Showcase.html', listings=listings_dict, page=page, total_pages=total_pages, query=search_query, sort=sort_by)
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred", 500
