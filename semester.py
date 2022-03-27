from flask import Blueprint, render_template, redirect, url_for, request
from models import tbl_semester
from flask_login import login_required, current_user
from __init__ import db

semester = Blueprint('semester', __name__)

@semester.route('/semester',methods=['GET']) 
@login_required
def semester_():
    semester = tbl_semester.query.all()
    return render_template('halaman_semester.html', semester=semester)

@semester.route('/semester/tambah', methods=['GET', 'POST', 'PUT']) 
@login_required
def tambah_semester():

    if request.method=='GET':
        return render_template('tambah_semester.html')

    id = request.form.get('id')
    catatan = request.form.get('catatan')

    new_semester = tbl_semester(kd_semester=id,catatan=catatan)
    db.session.add(new_semester)
    db.session.commit()
    
    return redirect(url_for('semester.semester_'))

@semester.route('/semester/edit/<int:id>', methods=['GET','POST']) 
@login_required
def edit_semester(id):

    if request.method=='GET':
        return render_template('tambah_semester_update.html')

    semester = tbl_semester.query.filter_by(kd_semester=id).first()
    semester.catatan = request.form.get('catatan')
    db.session.commit()
    
    return redirect(url_for('semester.semester_'))


@semester.route('/semester/hapus/<int:id>', methods=['GET','POST']) 
@login_required
def hapus_semester(id):
    semester = tbl_semester.query.filter_by(kd_semester=id).first()
    db.session.delete(semester)
    db.session.commit()
    
    return redirect(url_for('semester.semester_'))
