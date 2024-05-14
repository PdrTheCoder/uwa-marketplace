from flask import Blueprint, render_template
from uwamkp.models import Listing
from sqlalchemy import select
from uwamkp.models import db

showcase_bp = Blueprint('showcase', __name__, url_prefix='/showcase')

@showcase_bp.route('/')
def showcase():
    # Getting Product Data
    stmt = select(Listing).where(Listing.deleted == False).order_by(Listing.created_at.desc()).limit(12)
    listings = db.session.scalars(stmt).all()
    listings_dict = [listing.to_dict() for listing in listings]
    
    # Rendering Templates
    return render_template('Showcase.html', listings=listings_dict)
