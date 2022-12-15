from flask_sqlalchemy import SQLAlchemy
#* Creates a SQLAlchemy app
#* This is done outside to allow accessing from other files (eg. from models).
db = SQLAlchemy()