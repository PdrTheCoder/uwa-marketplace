# signup.py
from flask import render_template, Blueprint, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
import re  # Regular expression module for validating email
from flask_wtf import CSRFProtect
from uwamkp.models import User, db
bp = Blueprint('signup', __name__, url_prefix='/user')


# ======= signup ===========
@bp.route('/signup', methods=['GET','POST'])
def signup():
    print("Signup route accessed, method:", request.method) 
    print(url_for('signup.signup'))
    print("Data received:", request.form)
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        print("Email validation check...")
        if not re.match(r'^[a-zA-Z0-9._%+-]+\.uwa\.edu\.au$', email):
            #error = "Please enter a valid UWA email address."
            flash("Please enter a valid UWA email address.", 'error')
            #return render_template('signup.html', error=error)
            #return redirect(url_for('signup.signup'))
            return render_template('signup.html', form_data=form_data)

        print("User existence check...")
        user = User.query.filter_by(email=email).first()
        if user:
            #error = "An account with this email already exists."
            flash("An account with this email already exists.", 'error')
            #return render_template('signup.html', error=error)
            #return redirect(url_for('signup.signup'))
            return render_template('signup.html', form_data=form_data)

        print("Password match check...")
        if password != password2:
            #error = "Passwords do not match."
            flash("Passwords do not match.", 'error')
            #return render_template('signup.html', error=error)
            return redirect(url_for('signup.signup'))

        print("Password strength check...")
        if not validate_password(password):
            #error = "Password must contain at least one numeral and one uppercase and lowercase letter, and at least 8 characters."
            flash("Password must contain at least one numeral, one uppercase and lowercase letter, and at least 8 characters.", 'error')
            #return render_template('signup.html', error=error)
            #return redirect(url_for('signup.signup'))
            return render_template('signup.html', form_data=form_data)

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Database error: {str(e)}")
            flash("Failed to register. Please try again.", 'error')
            return render_template('signup.html')

        flash("You have successfully signed up! Please log in.", 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')

def validate_password(password):
    """ Check if the password is strong enough."""
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    return True

# ======= signup ===========


# ======= other views 1 ===========
# other
# ======= end other views 1 ===========


# ======= other views 2 ===========
# other
# ======= end other views 2 ===========


# ======= other views 3 ===========
# other
# ======= end other views 3 ===========
