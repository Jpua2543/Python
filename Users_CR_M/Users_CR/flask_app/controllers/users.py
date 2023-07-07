
from flask import render_template, request,redirect

from flask_app.models.user import User

from flask_app import app
@app.route("/")
def readall():
    users = User.get_all()
    return render_template("Read_All.html" ,users = users)

@app.route("/add", methods= ["POST"] )
def add():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "password":request.form["password"],
        "email": request.form["email"]
    }
    print(data)
    User.save(data)
    return redirect("/")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/user/readone/<int:id>")
def one_user(id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    user=User.get_one(id)
    return render_template("read_one.html",user=user)


@app.route("/user/edit/<int:id>")
def edit(id):
    return render_template("edit.html",user=User.get_one(id))

@app.route("/update", methods= ["POST"] )
def update():
    User.update(request.form)
    print(request)
    return redirect("/")


@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {
        'id':id
    }
    User.destroy(data)
    return redirect('/')