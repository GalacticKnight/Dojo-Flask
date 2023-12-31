from flask import Flask, render_template,redirect
app = Flask(__name__)

@app.route('/')
def level():
    return redirect("/play")

@app.route('/play')
def level_one():
    return render_template("index.html",num=3,color="blue")

@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)