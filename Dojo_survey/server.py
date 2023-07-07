from flask import Flask, render_template,redirect,session,request

app = Flask(__name__)
app.secret_key = 'Codeitwell'

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/data', methods=['POST'])
def create_survey():
    # Here we add two properties to session to store the name and email
    session["name"] = request.form["name"]
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

# import statements, maybe some other routes

@app.route('/result')
def result_page():
    return render_template('result.html')


# import statements, maybe some other routes

# @app.route('/success')
# def success():
#     return "success"




if __name__ =="__main__":
    app.run(debug=True)