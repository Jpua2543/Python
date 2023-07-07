from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'Code it'

@app.route('/')
def times():
    if 'times' not in session:
        session ['times'] = 0
    else:
        session ['times'] += 2
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")






if __name__=="__main__":
    app.run(debug=True)