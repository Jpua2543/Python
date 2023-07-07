from flask import render_template, request,redirect,session
from flask_app.models.user import User
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def login_and_registration():
    return render_template("login_and_registration.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/register", methods= ["POST"] )
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    one_user = User.save(data)
    if one_user:
        session['user_id']=one_user
        session['name'] = request.form['first_name']+ " " +request.form['last_name']
        return redirect("/recipes")
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    print('user_in_db>>>>>>>>>>',user_in_db)
    if not user_in_db:
        flash("Invalid Email/Password","log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password","log")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['name'] = user_in_db.first_name+ " "+ user_in_db.last_name
    return redirect("/recipes")