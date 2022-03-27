from flask import Blueprint, render_template, flash,request,redirect, url_for
from flask_login import login_required, current_user
from __init__ import create_app, db
from models import User


main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/dashboard') # profile page that return 'profile'
@login_required
def admin():
    return render_template('halaman_admin.html')    

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode