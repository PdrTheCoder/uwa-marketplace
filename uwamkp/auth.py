from datetime import datetime
from flask import Blueprint
from flask import flash
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from uwamkp.models import db
from uwamkp.models import User
from uwamkp.forms import LoginForm
from uwamkp.forms import RegistrationForm

from sqlalchemy import select
from werkzeug.security import generate_password_hash
import re  # Regular expression module for validating email and username


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=hashed_password,
                    # timezone-aware UTC datetime
                    created_at=datetime.now(datetime.utc),
                    is_admin=False,
                    deleted=False)
        db.session.add(user)
        try:
            db.session.commit()
            flash('You have been successfully registered. Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again. Error: {}'.format(e), 'error')
    return render_template('signup.html', form=form)


@bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    else:
        if form.is_submitted() and form.validate():
            stmt = select(User).where(User.email == form.email.data)
            user = db.session.scalars(stmt).one_or_none()
            if user and user.verify_password(form.password.data):
                login_user(user)
                return redirect(url_for("mylisting.my_listing"))
            else:
                flash('Wrong email and password combination \
                    or email does not exist', 'error')
        return render_template("login.html", form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for("auth.login"))
