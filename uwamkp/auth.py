from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from uwamkp.models import db
from uwamkp.models import User
from uwamkp.forms import LoginForm
from sqlalchemy import select


bp = Blueprint('auth', __name__, url_prefix='/auth')


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
