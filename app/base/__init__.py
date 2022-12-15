from flask import Blueprint

base = Blueprint("base", __name__)

@base.route("/")
def home():
    return "Homepage"