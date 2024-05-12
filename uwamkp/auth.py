from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from uwamkp.models import db
from uwamkp.models import User
from uwamkp.forms import LoginForm
from uwamkp.constants import INDEX_ANONYMOUS
from uwamkp.constants import INDEX_LOGGED
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
                login_user(user)
                return redirect(INDEX_LOGGED)
            else:
                flash('Wrong email and password combination \
                    or email does not exist', 'danger')
        return render_template("login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(INDEX_ANONYMOUS)
