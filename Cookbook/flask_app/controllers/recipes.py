from flask import render_template, request,redirect,session
from flask_app.models.user import User
from flask_app import app
from flask import flash


@app.route("/createnewrecipes")
def newrecipes():
    return render_template("new_recipes.html")

@app.route("/register", methods= ["POST"] )
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "DateCookd_Made": request.form['DateCookd_Made'],
        "Under_30_minutes": request.form['Under_30_minutes'],
        "Users_id": request.form['Users_id'],
    }
    one_user = User.save(data)
    if one_user:
        session['user_id']=one_user
        session['name'] = request.form['first_name']+ " " +request.form['last_name']
        return redirect("/recipes")
    return redirect("/")


