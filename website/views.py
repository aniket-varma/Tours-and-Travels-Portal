from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    return render_template("index.html")
@views.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        print("here")
        email=request.form.get('email')
        password=request.form.get('password')
        print(email)
        print(password)
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged In Successfully',category='Success')
                return redirect(url_for('views.home'))    
            else:
                flash('Invalid Login Credentials',category='Error')
    return render_template("login.html")
@views.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        password=request.form.get('password')
        confirm=request.form.get('confirm')
        
        if password!=confirm:
            flash('Password not matching',category='Error')
        elif len(password) < 8:
            flash('Paswword is too short. Must be 8 characters long.',category='Error')
        else:
            #add user to the database
            new_user=User(name=name,email=email,phone=phone,password=generate_password_hash(password,method='sha256'))
            print("here")
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created Successfully.',category='Success')
            return redirect(url_for('views.home'))
    return render_template("signup.html")
    