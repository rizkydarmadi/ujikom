from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class kd_dosen(UserMixin, db.Model):
    kd_dosen = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    nama = db.Column(db.String(100))
    alamat = db.Column(db.String(100))

