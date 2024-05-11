from datetime import datetime,timezone
from flask import render_template, Blueprint, request, redirect, url_for, flash
from uwamkp.models import db
from uwamkp.models import User
from uwamkp.forms import LoginForm,RegistrationForm
from sqlalchemy import select
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
import re  # Regular expression module for validating email and username


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data,
                    created_at=datetime.now(timezone.utc), # timezone-aware UTC datetime
                    is_admin=False,
                    deleted=False)
        db.session.add(user)
        db.session.commit()
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
                # TODO later change to main page
                return redirect('/mylisting/listings')
            else:
                flash('Wrong email and password combination \
                    or email does not exist', 'danger')
        return render_template("login.html", form=form)
    
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))




