from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="I am Lord Voldemort"

@app.route('/')
def index():
    if "count" in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template("index.html")

@app.route('/reset')
def reset():
    session['count'] =0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)