from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.trail import Trail
from flask_app.models.user import User


@app.route('/new/trail')
def newtrail():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data = {
        "id":session['user_id']
    }
    return render_template("newtrail.html",user=User.getOne(user_data))

@app.route('/create/trail',methods=['POST'])
def createtrail():
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
def edittrail(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    print(Trail.getOne(data).name)
    return render_template("edittrail.html",edit=Trail.getOne(data),user=User.getOne(user_data))

@app.route('/update/trail',methods=['POST'])
def updatetrail():
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
def showtrail(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("showtrail.html",trail=Trail.getOne(data),user=User.getOne(user_data))

@app.route('/destroy/trail/<int:id>')
def deletetrail(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Trail.delete(data)
    return redirect('/dashboard')