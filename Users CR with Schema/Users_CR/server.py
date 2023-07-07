from flask import Flask, render_template, request,redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route("/")
def readall():
    users = User.get_all()
    return render_template("Read_All.html" ,users = users)

@app.route("/add", methods= ["POST"] )
def add():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
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

if __name__ == "__main__":
    app.run(debug=True)
