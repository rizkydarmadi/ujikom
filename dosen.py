from flask import Blueprint, render_template, redirect, url_for, request
from models import tbl_dosen
from flask_login import login_required, current_user
from __init__ import db

dosen = Blueprint('dosen', __name__)

@dosen.route('/dosen',methods=['GET']) 
@login_required
def dosen_():
    dosen = tbl_dosen.query.all()
    return render_template('halaman_dosen.html', dosen=dosen)

@dosen.route('/dosen/tambah', methods=['GET', 'POST', 'PUT']) 
@login_required
def tambah_dosen():

    if request.method=='GET':
        return render_template('tambah_dosen.html')

    id = request.form.get('id')
    nama = request.form.get('nama')
    alamat = request.form.get('alamat')

    new_dosen = tbl_dosen(kd_dosen=id,nama=nama,alamat=alamat)
    db.session.add(new_dosen)
    db.session.commit()
    
    return redirect(url_for('dosen.dosen_'))

@dosen.route('/dosen/edit/<int:id>', methods=['GET','POST']) 
@login_required
def edit_dosen(id):

    if request.method=='GET':
        return render_template('tambah_dosen_update.html')

    dosen = tbl_dosen.query.filter_by(kd_dosen=id).first()
    dosen.nama = request.form.get('nama')
    dosen.alamat = request.form.get('alamat')
    db.session.commit()
    
    return redirect(url_for('dosen.dosen_'))


@dosen.route('/dosen/hapus/<int:id>', methods=['GET','POST']) 
@login_required
def hapus_dosen(id):
    dosen = tbl_dosen.query.filter_by(kd_dosen=id).first()
    db.session.delete(dosen)
    db.session.commit()
    
    return redirect(url_for('dosen.dosen_'))
