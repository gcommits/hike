from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.trail import Trail
from flask_app.models.user import User


@app.route('/new/trail')
def new_trail():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data = {
        "id":session['user_id']
    }
    return render_template("new_trail.html",user=User.getOne(user_data))

@app.route('/create/trail',methods=['POST'])
def create_trail():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Trail.validate(request.form):
        return redirect('/new/trail')
    data = {
        "img": request.form["img"],
        "name": request.form["name"],
        "location": request.form["location"],
        "difficulty": request.form["difficulty"],
        "rating": request.form["rating"],
        "dateCompleted": request.form["dateCompleted"],
        "elevationGain": request.form["elevationGain"],
        "length": request.form["length"],
        "routeType": request.form["routeType"],
        "comments": request.form["comments"],
        "user_id": session["user_id"]
    }
    Trail.save(data)
    return redirect('/dashboard')

@app.route('/edit/trail/<int:id>')
def edit_trail(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    print(Trail.getOne(data).name)
    return render_template("edit_trail.html",edit=Trail.getOne(data),user=User.getOne(user_data))

@app.route('/update/trail',methods=['POST'])
def update_trail():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Trail.validate(request.form):
        return redirect(f'/edit/trail/{request.form["id"]}')
    data = {
        "img": request.form["img"],
        "name": request.form["name"],
        "location": request.form["location"],
        "difficulty": request.form["difficulty"],
        "rating": request.form["rating"],
        "dateCompleted": request.form["dateCompleted"],
        "elevationGain": request.form["elevationGain"],
        "length": request.form["length"],
        "routeType": request.form["routeType"],
        "comments": request.form["comments"],
        "id": request.form['id']
    }
    Trail.update(data)
    return redirect('/dashboard')

@app.route('/trail/<int:id>')
def show_trail(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_trail.html",trail=Trail.getOne(data),user=User.getOne(user_data))

@app.route('/destroy/trail/<int:id>')
def delete_trail(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Trail.delete(data)
    return redirect('/dashboard')