from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')#DEFAULT ROUTE. IF YOU OPEN WITH NOTHING, IT GOES STRAIGHT HERE
def index():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html",users=users)#IT ACTIVATES THIS INDEX FILE YOU MADE THAT WILL PRESENT EVERYTHING AND WHAT YOU SAVE AS USERS WHICH IS THE DICTIONARY IS GOING TO BE USERS
if __name__=="__main__":
    app.run(debug=True)