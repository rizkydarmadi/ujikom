from flask import Blueprint, render_template, redirect, url_for, request
from models import tbl_jadwal,tbl_dosen, tbl_mahasiswa, tbl_matkul,tbl_krs, tbl_semester
from flask_login import login_required, current_user
from __init__ import db
import datetime

krs = Blueprint('krs', __name__)

@krs.route('/krs',methods=['GET']) 
@login_required
def krs_():
    krs = tbl_krs.query.with_entities(tbl_krs.kd_krs,tbl_dosen.nama.label("dosen"),tbl_matkul.nama.label("matkul"),tbl_semester.kd_semester.label("semester"),tbl_mahasiswa.nama.label("mahasiswa"),tbl_jadwal.waktu.label("waktu"))\
    .join(tbl_dosen,tbl_krs.kd_dosen==tbl_dosen.kd_dosen)\
    .join(tbl_matkul,tbl_krs.kd_matkul==tbl_matkul.kd_matkul)\
    .join(tbl_semester,tbl_krs.kd_semester==tbl_semester.kd_semester)\
    .join(tbl_mahasiswa,tbl_krs.kd_mahasiswa==tbl_mahasiswa.kd_mahasiswa)\
    .join(tbl_jadwal,tbl_krs.kd_jadwal==tbl_jadwal.id)\
    .all()
   
    return render_template('halaman_krs.html', krs=krs)


@krs.route('/krs/tambah', methods=['GET', 'POST', 'PUT']) 
@login_required
def tambah_krs():

    if request.method=='GET':
        return render_template('tambah_krs.html')


    id = request.form.get('id')


    mahasiswa_id = db.session.query(tbl_mahasiswa.kd_mahasiswa).filter(tbl_mahasiswa.nama==request.form.get('mahasiswa')).first()
    if mahasiswa_id is None:
        return "<h1> masukan nama mahasiswa dengan benar </h1>"
    mahasiswa_id = mahasiswa_id.kd_mahasiswa

    semester_id = db.session.query(tbl_semester.kd_semester).filter(tbl_semester.kd_semester==request.form.get('semester')).first()
    if semester_id is None:
        return "<h1> masukan nama semester dengan benar </h1>"
    semester_id = semester_id.kd_semester

    dosen_id = db.session.query(tbl_dosen.kd_dosen).filter(tbl_dosen.nama==request.form.get('dosen')).first()
    if dosen_id is None:
        return "<h1> masukan nama dosen dengan benar </h1>"
    kd_dosen = dosen_id.kd_dosen

    matkul_id = db.session.query(tbl_matkul.kd_matkul).filter(tbl_matkul.nama==request.form.get('matkul')).first()
    if matkul_id is None:
        return "<h1> masukan nama matkul dengan benar </h1>"    
    matkul_id = matkul_id.kd_matkul

    # d, m, y = request.form.get('jadwal').split('-')
    # jadwal = datetime.datetime(int(y), int(m), int(d))
    # jadwal_id = db.session.query(tbl_jadwal.id).filter(tbl_jadwal.id==jadwal).first()
    # if jadwal_id is None:
    #     return "<h1> masukan waktu jadwal dengan benar </h1>"
    # jadwal_id= jadwal_id.id
  
    new_jadwal = tbl_krs(kd_krs=id,kd_mahasiswa=mahasiswa_id,kd_semester=semester_id,kd_dosen=kd_dosen,kd_jadwal=int(9828),kd_matkul=matkul_id)
    db.session.add(new_jadwal)
    db.session.commit()

    return redirect(url_for('krs.krs_'))

# @krs.route('/krs/edit/<int:id>', methods=['GET','POST']) 
# @login_required
# def edit_jadwal(id):

#     if request.method=='GET':
#         return render_template('tambah_jadwal_update.html')

#     krs = tbl_jadwal.query.filter_by(id=id).first()

#     dosen_id = db.session.query(tbl_dosen.kd_dosen).filter(tbl_dosen.nama==request.form.get('dosen')).first()
#     if dosen_id is None:
#         return "<h1> masukan nama dosen dengan benar </h1>"
#     kd_dosen = dosen_id.kd_dosen
#     matkul_id = db.session.query(tbl_matkul.kd_matkul).filter(tbl_matkul.nama==request.form.get('kd_matkul')).first()
#     if matkul_id is None:
#         return "<h1> masukan nama matkul dengan benar </h1>"
#     matkul = matkul_id.kd_matkul

#     krs.kd_dosen = kd_dosen
#     krs.kd_matkul = matkul
#     krs.ruang = request.form.get('ruang')

#     d, m, y = request.form.get('waktu').split('-')
#     krs.waktu = datetime.datetime(int(y), int(m), int(d))
    
#     db.session.commit()
    
#     return redirect(url_for('krs.jadwal_'))

# @krs.route('/krs/hapus/<int:id>', methods=['GET','POST']) 
# @login_required
# def hapus_dosen(id):
#     krs = tbl_jadwal.query.filter_by(id=id).first()
#     db.session.delete(krs)
#     db.session.commit()
    
#     return redirect(url_for('krs.jadwal_'))