from datetime import datetime
from datetime import timezone
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import render_template
from flask import flash
from flask import current_app
from flask_login import current_user
from flask_login import login_required
import os
import uuid
from uwamkp.models import db
from uwamkp.models import Listing
from uwamkp.models import Reply
from uwamkp.product_forms import PublishForm
from uwamkp.product_forms import MessageForm
from werkzeug.utils import secure_filename
from sqlalchemy import desc

bp = Blueprint('product', __name__)


def save_and_return_paths(photo_form):
    """save photo file to local disk.
    Also return the relative_path that is relative to static folder
    """
    f = photo_form.photo.data
    if f:
        filename = secure_filename(f.filename)
        # to avoid dup filename
        filename = str(uuid.uuid4())[:8] + '_' + filename
        abs_filepath = os.path.join(
            current_app.static_folder,
            current_app.config["PHOTO_FOLDER"], filename
        )
        f.save(abs_filepath)
        return current_app.config["PHOTO_FOLDER"] + '/' + filename
    else:
        return


@bp.route('/addproduct', methods=['GET', 'POST'])
@login_required
def addproduct():
    form = PublishForm()
    if form.validate_on_submit():
        relative_path = save_and_return_paths(form)

        if not relative_path:
            flash('Failed to get the photo of the listing.', 'danger')
            return render_template("addproduct.html", form=form)

        try:
            new_listing = Listing(
                title=form.title.data, price=form.price.data,
                condition=form.condition.data,
                description=form.description.data,
                seller_id=current_user.id,
                suspended=False,
                sold=False,
                deleted=False,
                created_at=datetime.now(timezone.utc),
                image_path=relative_path
            )
            db.session.add(new_listing)
            db.session.commit()
            flash('Your listing has been added!', 'success')
            return redirect(url_for('mylisting.my_listing'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding product.', 'danger')
            # TODO If saving fails, also remember to delete the file
            return render_template("addproduct.html", form=form)
    return render_template("addproduct.html", form=form)


@bp.route('/details/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def details(listing_id):
    listing = db.session.query(Listing).get(listing_id)
    form = MessageForm()
    if form.validate_on_submit():
        new_message = Reply(
            message=form.messageContent.data,
            listing_id=listing_id,
            from_user_id=current_user.id,
            created_at=datetime.now(timezone.utc)
        )
        db.session.add(new_message)
        db.session.commit()
        flash('Message posted!', 'success')
        form = MessageForm()
        messages = db.session.query(Reply).filter_by(listing_id=listing_id).order_by(desc(Reply.created_at)).all()
        return render_template('details.html', listing=listing.to_dict(), form=form, messages=messages)
    messages = db.session.query(Reply).filter_by(listing_id=listing_id).order_by(desc(Reply.created_at)).all()
    return render_template('details.html', listing=listing.to_dict(), form=form, messages=messages)


@bp.route('/update/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def edit(listing_id: int):
    listing = db.session.query(Listing).get(listing_id)
    form = PublishForm(obj=listing)

    if form.validate_on_submit():
        relative_path = save_and_return_paths(form)

        if not relative_path:
            flash('Failed to get the photo of the listing.', 'danger')
            return render_template("addproduct.html", form=form)

        listing.title = form.title.data
        listing.price = form.price.data
        listing.condition = form.condition.data
        listing.description = form.description.data
        listing.updated_at = datetime.now(timezone.utc)
        listing.image_path = relative_path
        try:
            db.session.commit()
            flash('Your listing has been successfully update', 'success')
            return redirect(url_for('mylisting.my_listing'))
        except Exception as e:
            db.session.rollback()
            flash("Error updating listing", "danger")
            return render_template('updateproduct.html', form=form, listing=listing)
    return render_template('updateproduct.html', form=form, listing=listing)
