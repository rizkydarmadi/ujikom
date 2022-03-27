from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class tbl_dosen(db.Model):
    kd_dosen = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    nama = db.Column(db.String(100))
    alamat = db.Column(db.String(100))

class tbl_matkul(db.Model):
    kd_matkul = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    nama = db.Column(db.String(100))
    sks = db.Column(db.Integer)

class tbl_jadwal(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    kd_dosen = db.Column(db.Integer,db.ForeignKey(tbl_dosen.kd_dosen),nullable=False)
    kd_matkul = db.Column(db.Integer,db.ForeignKey(tbl_matkul.kd_matkul),nullable=False)
    ruang = db.Column(db.Integer)
    waktu = db.Column(db.DateTime(100),nullable=False)

class tbl_mahasiswa(db.Model):
    kd_mahasiswa = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    nama = db.Column(db.String(100))
    jurusan = db.Column(db.String(100))

class tbl_semester(db.Model):
    kd_semester = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    catatan = db.Column(db.String(100))

class tbl_krs(db.Model):
    kd_krs = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    kd_mahasiswa = db.Column(db.Integer, db.ForeignKey(tbl_mahasiswa.kd_mahasiswa),nullable=False)
    kd_semester = db.Column(db.Integer, db.ForeignKey(tbl_semester.kd_semester),nullable=False) 
    kd_dosen = db.Column(db.Integer, db.ForeignKey(tbl_dosen.kd_dosen),nullable=False)
    kd_jadwal = db.Column(db.Integer, db.ForeignKey(tbl_jadwal.id),nullable=False) 
    kd_matkul = db.Column(db.Integer, db.ForeignKey(tbl_matkul.kd_matkul),nullable=False) 




   


