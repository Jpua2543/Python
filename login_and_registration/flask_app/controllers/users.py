from flask import render_template, request,redirect,session

from flask_app.models.user import User

from flask_app import app

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/dashboard")
def dashboardpage():
    return render_template("dashboard.html")


@app.route("/save", methods= ["POST"] )
def add():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password":request.form["password"]
    }
    print(request.form)
    User.save(data)
    return redirect("/")


# @app.route('/register', methods=['POST'])
# def save():
#     # if not User.validate_user(request.form):
#     #     # we redirect to the template with the form.
#     #     return redirect('/')
#     # ... do other things
#     data = {
#         "first_name": request.form['first_name'],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"],
#         "password":request.form["password"]
#     }
#     User.save(data)
#     return redirect('/dashboard')