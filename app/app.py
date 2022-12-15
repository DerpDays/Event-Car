from flask import Flask
from .database import db
from .base import base
from .auth import auth
from .api import api

def create_app(cfg):
    #* Creates the flask app.
    app = Flask(__name__)
    #* Loads the config from the parameter provided.
    app.config.from_object(cfg)
    
    #* Links the extension with the app and creates tables for all models that are used in the app.
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    #* Registers the blueprints of each section of the app.
    app.register_blueprint(base)
    app.register_blueprint(auth)
    app.register_blueprint(api)
    #* Returns the application so it can be used elsewhere (i.e. to run the app)
    return app
