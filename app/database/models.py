# from .. import db

# class User(db.Model):
#     id = db.Column(type=db.Integer, auto_increment=True, primary_key=True)
#     email = db.Column(type=db.String(64), unique=True)
#     password = db.Column(type=db.String(50))
#     firstname = db.Column(type=db.String(50))
#     lastname = db.Column(type=db.String(50))
#     dateofbirth = db.Column(type=db.Date)
#     lastupdated = db.Column(type=db.DateTime, default=db.funcs.now())
#     createdat = db.Column(type=db.DateTime, default=db.funcs.now())

from sqlalchemy.sql.functions import now
from . import db

class User(db.Model):
    __tablename__ = 'users'
  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False, default=now())
    created_at = db.Column(db.DateTime, nullable=False, default=now())
    
    def __repr__(self):
        return f"<User {self.email}>"
    
# class User(db.Model):
#     """Data model for user accounts."""

#     __tablename__ = "flasksqlalchemy-tutorial-users"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True, nullable=False)
#     email = db.Column(db.String(80), index=True, unique=True, nullable=False)
#     created = db.Column(db.DateTime, nullable=False)
#     bio = db.Column(db.Text, nullable=True)
#     admin = db.Column(db.Boolean, nullable=False)

#     def __repr__(self):
#         return "<User {}>".format(self.username)