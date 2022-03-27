from flask import Blueprint, render_template, flash,request
from flask_login import login_required, current_user
from __init__ import create_app, db
from models import User,kd_dosen


main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/dashboard') # profile page that return 'profile'
@login_required
def admin():
    return render_template('halaman_admin.html')

@main.route('/dosen',methods=['GET', 'PUT', 'DELETE']) # profile page that return 'profile'
@login_required
def dosen():
    dosen = kd_dosen.query.all()
    return render_template('halaman_dosen.html', dosen=dosen)

@main.route('/dosen/tambah', methods=['GET', 'POST']) # profile page that return 'profile'
@login_required
def tambah_dosen():
    dosen = kd_dosen.query.all()
    # text = request.form['nama dosen']
    # print(text)
    id = request.form.get('id')
    nama = request.form.get('nama')
    alamat = request.form.get('alamat')

    new_dosen = kd_dosen(kd_dosen=id,nama=nama,alamat=alamat)
    db.session.add(new_dosen)
    db.session.commit()
    
    return render_template('tambah_dosen.html', dosen=dosen)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode