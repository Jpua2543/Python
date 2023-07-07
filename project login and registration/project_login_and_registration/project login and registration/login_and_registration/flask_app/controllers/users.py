from flask import render_template, request,redirect,session

from flask_app.models.user import User

from flask_app import app

from flask import flash

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if session.get('user_id'):
        return render_template("dashboard.html")
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/save", methods= ["POST"] )
def add():
    if not User.validate_user(request.form):
        return redirect('/')
    session['name'] = request.form['first_name']+ " " +request.form['last_name']
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    if User.save(data):
        return redirect("/dashboard")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    print('user_in_db>>>>>>>>>>',user_in_db)# debugging success 
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/create")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['name'] = user_in_db.first_name+ " "+ user_in_db.last_name
    return redirect("/dashboard")
