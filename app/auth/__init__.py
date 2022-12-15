from flask import Blueprint

auth = Blueprint('auth', __name__)

from .routes import Login, Signup, home


auth.add_url_rule("/users/", view_func=home)
auth.add_url_rule("/login/", view_func=Login.as_view("login"))
auth.add_url_rule("/signup/", view_func=Signup.as_view("signup"))
