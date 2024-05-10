# signup.py
from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
import re  # Regular expression module for validating email
from flask_wtf import CSRFProtect
from uwamkp.models import User,db
from .forms import LoginForm, RegistrationForm
bp = Blueprint('signup', __name__, url_prefix='/signup')


# ======= signup_login_logout ===========
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('signup.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid email or password.')
    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
# ======= signup_login_logout ===========


# ======= other views 1 ===========
# other
# ======= end other views 1 ===========


# ======= other views 2 ===========
# other
# ======= end other views 2 ===========


# ======= other views 3 ===========
# other
# ======= end other views 3 ===========
