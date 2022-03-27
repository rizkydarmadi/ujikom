from flask import Blueprint, render_template, redirect, url_for, request
from models import tbl_matkul
from flask_login import login_required, current_user
from __init__ import db

matkul = Blueprint('matkul', __name__)

@matkul.route('/matkul',methods=['GET']) 
@login_required
def matkul_():
    matkul = tbl_matkul.query.all()
    return render_template('halaman_matkul.html', matkul=matkul)

@matkul.route('/matkul/tambah', methods=['GET', 'POST', 'PUT']) 
@login_required
def tambah_matkul():

    if request.method=='GET':
        return render_template('tambah_matkul.html')

    id = request.form.get('id')
    nama = request.form.get('nama')
    sks = request.form.get('sks')

    new_matkul = tbl_matkul(kd_matkul=id,nama=nama,sks=sks)
    db.session.add(new_matkul)
    db.session.commit()

    return redirect(url_for('matkul.matkul_'))

@matkul.route('/matkul/edit/<int:id>', methods=['GET','POST']) 
@login_required
def edit_matkul(id):

    if request.method=='GET':
        return render_template('tambah_matkul_update.html')

    matkul = tbl_matkul.query.filter_by(kd_matkul=id).first()
    matkul.nama = request.form.get('nama')
    matkul.sks = request.form.get('sks')
    db.session.commit()
    
    return redirect(url_for('matkul.matkul_'))

@matkul.route('/matkul/hapus/<int:id>', methods=['GET','POST']) 
@login_required
def hapus_dosen(id):
    matkul = tbl_matkul.query.filter_by(kd_matkul=id).first()
    db.session.delete(matkul)
    db.session.commit()
    
    return redirect(url_for('matkul.matkul_'))