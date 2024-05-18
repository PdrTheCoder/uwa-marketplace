from datetime import datetime
from flask import Blueprint, flash, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from uwamkp.models import db, User
from uwamkp.forms import LoginForm, RegistrationForm
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
                    created_at=datetime.utcnow(),  # timezone-aware UTC datetime
                    is_admin=False,
                    deleted=False)
        db.session.add(user)
        try:
            db.session.commit()
            flash('You have been successfully registered. Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again. Error: {}'.format(e), 'danger')
    return render_template('signup.html', form=form)


@bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    next_page = request.args.get('next')  # Get 'next' parameter from URL

    if request.method == "GET":
        return render_template("login.html", form=form, next=next_page)
    else:
        if form.is_submitted() and form.validate():
            stmt = select(User).where(User.email == form.email.data)
            user = db.session.scalars(stmt).one_or_none()
            if user and user.verify_password(form.password.data):
                login_user(user)
                return redirect(next_page or url_for("showcase.showcase"))  # Redirect to 'next' page if available
            else:
                flash('Wrong email and password combination or email does not exist', 'danger')
        return render_template("login.html", form=form, next=next_page)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for("auth.login"))


@bp.route('/is_logged_in')
def is_logged_in():
    return jsonify(logged_in=current_user.is_authenticated)

