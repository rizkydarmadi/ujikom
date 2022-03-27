from flask import Blueprint, render_template, redirect, url_for, request
from models import tbl_jadwal,tbl_dosen, tbl_matkul
from flask_login import login_required, current_user
from __init__ import db
import datetime

jadwal = Blueprint('jadwal', __name__)

@jadwal.route('/jadwal',methods=['GET']) 
@login_required
def jadwal_():
    jadwal = tbl_jadwal.query.with_entities(tbl_jadwal.id,tbl_dosen.nama.label("nama_dosen"),tbl_matkul.nama.label("nama_matkul"),tbl_jadwal.ruang,tbl_jadwal.waktu)\
    .join(tbl_dosen,tbl_jadwal.kd_dosen==tbl_dosen.kd_dosen)\
    .join(tbl_matkul,tbl_jadwal.kd_matkul==tbl_matkul.kd_matkul)\
    .all()
    
   
    return render_template('halaman_jadwal.html', jadwal=jadwal)


@jadwal.route('/jadwal/tambah', methods=['GET', 'POST', 'PUT']) 
@login_required
def tambah_jadwal():

    if request.method=='GET':
        return render_template('tambah_jadwal.html')


    id = request.form.get('id')

    dosen_id = db.session.query(tbl_dosen.kd_dosen).filter(tbl_dosen.nama==request.form.get('dosen')).first()
    if dosen_id is None:
        return "<h1> masukan nama dosen dengan benar </h1>"
    kd_dosen = dosen_id.kd_dosen
    matkul_id = db.session.query(tbl_matkul.kd_matkul).filter(tbl_matkul.nama==request.form.get('kd_matkul')).first()
    if matkul_id is None:
        return "<h1> masukan nama matkul dengan benar </h1>"
    matkul = matkul_id.kd_matkul

    

    ruang = request.form.get('ruang')

    d, m, y = request.form.get('waktu').split('-')
    waktu = datetime.datetime(int(y), int(m), int(d))

    new_jadwal = tbl_jadwal(id=id,kd_dosen=kd_dosen,kd_matkul=matkul,ruang=ruang,waktu=waktu)
    db.session.add(new_jadwal)
    db.session.commit()

    return redirect(url_for('jadwal.jadwal_'))

@jadwal.route('/jadwal/edit/<int:id>', methods=['GET','POST']) 
@login_required
def edit_jadwal(id):

    if request.method=='GET':
        return render_template('tambah_jadwal_update.html')

    jadwal = tbl_jadwal.query.filter_by(id=id).first()

    dosen_id = db.session.query(tbl_dosen.kd_dosen).filter(tbl_dosen.nama==request.form.get('dosen')).first()
    if dosen_id is None:
        return "<h1> masukan nama dosen dengan benar </h1>"
    kd_dosen = dosen_id.kd_dosen
    matkul_id = db.session.query(tbl_matkul.kd_matkul).filter(tbl_matkul.nama==request.form.get('kd_matkul')).first()
    if matkul_id is None:
        return "<h1> masukan nama matkul dengan benar </h1>"
    matkul = matkul_id.kd_matkul

    jadwal.kd_dosen = kd_dosen
    jadwal.kd_matkul = matkul
    jadwal.ruang = request.form.get('ruang')

    d, m, y = request.form.get('waktu').split('-')
    jadwal.waktu = datetime.datetime(int(y), int(m), int(d))
    
    db.session.commit()
    
    return redirect(url_for('jadwal.jadwal_'))

@jadwal.route('/jadwal/hapus/<int:id>', methods=['GET','POST']) 
@login_required
def hapus_dosen(id):
    jadwal = tbl_jadwal.query.filter_by(id=id).first()
    db.session.delete(jadwal)
    db.session.commit()
    
    return redirect(url_for('jadwal.jadwal_'))