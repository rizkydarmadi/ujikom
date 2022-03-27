from flask import Blueprint, render_template, redirect, url_for, request
from models import tbl_mahasiswa
from flask_login import login_required, current_user
from __init__ import db

mahasiswa = Blueprint('mahasiswa', __name__)

@mahasiswa.route('/mahasiswa',methods=['GET']) 
@login_required
def mahasiswa_():
    mahasiswa = tbl_mahasiswa.query.all()
    return render_template('halaman_mahasiswa.html', mahasiswa=mahasiswa)

@mahasiswa.route('/mahasiswa/tambah', methods=['GET', 'POST', 'PUT']) 
@login_required
def tambah_mahasiswa():

    if request.method=='GET':
        return render_template('tambah_mahasiswa.html')

    id = request.form.get('id')
    nama = request.form.get('nama')
    jurusan = request.form.get('jurusan')

    new_mahasiswa = tbl_mahasiswa(kd_mahasiswa=id,nama=nama,jurusan=jurusan)
    db.session.add(new_mahasiswa)
    db.session.commit()

    return redirect(url_for('mahasiswa.mahasiswa_'))

@mahasiswa.route('/mahasiswa/edit/<int:id>', methods=['GET','POST']) 
@login_required
def edit_mahasiswa(id):

    if request.method=='GET':
        return render_template('tambah_mahasiswa_update.html')

    mahasiswa = tbl_mahasiswa.query.filter_by(kd_mahasiswa=id).first()
    mahasiswa.nama = request.form.get('nama')
    mahasiswa.jurusan = request.form.get('jurusan')
    db.session.commit()
    
    return redirect(url_for('mahasiswa.mahasiswa_'))

@mahasiswa.route('/mahasiswa/hapus/<int:id>', methods=['GET','POST']) 
@login_required
def hapus_dosen(id):
    mahasiswa = tbl_mahasiswa.query.filter_by(kd_mahasiswa=id).first()
    db.session.delete(mahasiswa)
    db.session.commit()
    
    return redirect(url_for('mahasiswa.mahasiswa_'))