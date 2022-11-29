from . import db 
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(255),unique=True)
    phone=db.Column(db.String(10),unique=True)
    password=db.Column(db.String(50))
    
    