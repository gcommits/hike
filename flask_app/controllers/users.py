from flask import render_template,redirect,session,request, flash, url_for, abort
from flask_app import app
from flask_app.models.user import User
from flask_app.models.trail import Trail
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def registerUser():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/register')
    data ={ 
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login')
def loginUser():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    user = User.getEmail(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html", user=User.getOne(data), trail=Trail.getAll()) #need to know what the html file will be for homepage after logging in.

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')