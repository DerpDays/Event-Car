import bcrypt
from flask.views import MethodView
from flask import flash, redirect, request, current_app, render_template, url_for
from ..database.models import db, User
from datetime import datetime
from .utils import check_email, check_birthday


def home():
    res = db.session.execute(db.select(User)).all()
    print(res)
    # for i in res.all(): print(i)
    return "Auth Routes"

class Login(MethodView):
    def get(self):
        return render_template("login.html")
    def post(self):
        email = request.form.get ("email")
        password = request.form.get("password")
        if email and password:
            pw = db.session.execute(db.select(User.password).where(User.email == email)).scalar_one_or_none()
            if pw:
                loggedIn = bcrypt.checkpw(password.encode("utf-8"), pw.encode("utf-8"))
                print(loggedIn)

class Signup(MethodView):
    def get(self):
        return render_template("signup.html")
    
    def post(self):
        # Fetching submitted form data from the incoming request.
        email = request.form.get("email")
        password = request.form.get("password").strip()
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        birthday = request.form.get("birthday")
        
        
        # Checks if all of the fields exist.
        if not check_email(email):
            flash("Please enter a valid email.")
            return redirect(url_for("auth.signup"))
        if not check_email(email):
            flash("Please enter a valid password.")
            return redirect(url_for("auth.signup"))
        if not check_email(email):
            flash("Please enter a valid email.")
            return redirect(url_for("auth.signup"))
        if not check_birthday(birthday):
            flash("You need to be over 18 to use this service.")
            return redirect(url_for("auth.signup"))
        if not all([firstname, lastname]):
            flash("Please enter a name.")
            return redirect(url_for("auth.signup"))

        exists = db.session.execute(db.select(User).where(User.email == email)).scalar_one_or_none()
        if exists:
            flash("This email is already in use.")
            return redirect(url_for("auth.signup"))
        # print(current_app.config.get("SECRET_KEY"))
        pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        user = User(
            email=email,
            password=pw,
            first_name=firstname,
            last_name=lastname,
            date_of_birth=date
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("base.home"))