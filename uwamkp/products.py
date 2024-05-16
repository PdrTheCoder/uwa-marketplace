from flask import Blueprint
from datetime import datetime
from datetime import timezone
from flask import redirect
from flask import url_for
from flask import render_template
from flask import flash
from flask_login import current_user
from flask_login import login_required
from uwamkp.models import db
from uwamkp.models import Listing
from uwamkp.models import Reply
from uwamkp.product_forms import PublishForm
from uwamkp.product_forms import MessageForm

bp = Blueprint('product', __name__)


@bp.route('/addproduct', methods=['GET', 'POST'])
@login_required
def addproduct():
    # username = current_user.username
    # email = current_user.email
    # created_at = current_user.created_at.isoformat(sep=" ", timespec="seconds")
    form = PublishForm()
    if form.validate_on_submit():
        try:
            new_listing = Listing(title=form.title.data,
                                  price=form.price.data,
                                  condition=form.condition.data,
                                  description=form.description.data,
                                  seller_id=current_user.id,
                                  suspended=False,
                                  sold=False,
                                  deleted=False,
                                  created_at=datetime.now(timezone.utc)
                                  )
            db.session.add(new_listing)
            db.session.commit()
            flash('Your listing has been added!', 'success')
            return redirect(url_for('mylisting.my_listing'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding product.', 'error')
            return render_template("addproduct.html", form=form)
    return render_template("addproduct.html", form=form)


@bp.route('/details/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def details(listing_id):
    listing = db.session.query(Listing).get(listing_id)
    form = MessageForm()
    if form.validate_on_submit():
        new_message = Reply(content=form.messageContent.data,
                            listing_id=listing_id,
                            message=form.messageContent.data,
                            from_user_id=current_user.id,
                            created_at=datetime.now(timezone.utc)
                            )
        db.session.add(new_message)
        db.session.commit()
        flash('Message posted!')
        return redirect(url_for('details', listing=listing.to_dict()))
    messages = db.session.query(Reply).filter_by(listing_id=listing_id).all()
    return render_template('details.html', listing=listing.to_dict(), form=form, messages=messages)


@bp.route('/update/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def edit(listing_id: int):
    listing = db.session.query(Listing).get(listing_id)
    form = PublishForm(obj=listing)
    if form.validate_on_submit():
        listing.title = form.title.data
        listing.price = form.price.data
        listing.condition = form.condition.data
        listing.description = form.description.data
        listing.updated_at = datetime.now(timezone.utc)
        try:
            db.session.commit()
            flash('Your listing has been successfully update', 'success')
            return redirect(url_for('mylisting.my_listing'))
        except Exception as e:
            db.session.rollback()
            flash("Error updating listing", "error")
            return render_template('updateproduct.html', form=form)
    return render_template('updateproduct.html', form=form)
