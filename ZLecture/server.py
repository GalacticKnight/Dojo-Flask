from flask import Flask, render_template #YOU NEED THIS 
#YOU NEED RENDER_TEMPLATE TO RENDER THE TEMPLATE FOLDER THAT WILL CONTAIN HTML FILES
app = Flask(__name__) #YOU NEED THIS

@app.route('/')#IF YOU LAUNCH THE WEBSITE, THIS WILL ACTIVATE THE FUNCTIONS BELOW SPECIFICALLY ONLY THIS ROUTE
def rootroute():
    print("this is")#THIS SHOWS UP IN THE TERMINAL when you enter the website
    return "Hello World"#THIS WILL PRINT OUT "HELLO WORLD"

@app.route('/qwerty')#IF YOU LAUNCH THE WEBSITE AND PUT /QWERTY AFTER THE LINK ON TOP, THIS WILL ACTIVATE THE FUNCTIONS BELOW SPECIFICALLY ONLY THIS ROUTE
def qwerty():#THIS MUST BE A DIFFERENT NAMED FUNCTION THAN OTHER FUNCTION
    print("this is not")#THIS SHOWS UP IN THE TERMINAL
    return "Hello World to you"

@app.route('/home')
def dashboard():
    return "ASHE! We got trouble!" 

@app.route('/say/<word>')#IF YOU WRITE IT LIKE THIS, WHAT EVER WORD YOU PUT IN, ITS GETS SAVED AS A VALUE
def hello(word):
    print(word)
    print(type(word))
    return "Hello "+word

@app.route('/saying/<word>/<int:num>')#IF YOU WRITE IT LIKE THIS, WHAT EVER WORD YOU PUT IN, ITS GETS SAVED AS A VALUE
def helloworld(word,num):
    share ="no"
    return share+" "+word*num

@app.route('/format/<word>')#IF YOU WRITE IT LIKE THIS, WHAT EVER WORD YOU PUT IN, ITS GETS SAVED AS A VALUE
def format(word):
    return f"Hello {word}"

@app.route('/template')#
def template():
    return render_template("index.html")

@app.route('/template2')#
def template2():
    return render_template("index.html", phrase= "Welcome to the internet", num=10)#YOU CAN PASS ANY VARIABLES TO THE HTML

@app.route('/lists')
def renderLists():
    studentInfo = [
        {'name':'Timmy Jimmy-Jam','age' : 35},
        {'name':'Bod Builder','age' : 5},
        {'name':'Atticus Zoo','age' : 3},
        {'name':'Aarc Zoo','age' : 20}
    ]
    return render_template('lists.html', students = studentInfo, list=[1,2,3,4,5])#YOU CAN HAVE MULTIPLE HTML IN YOUR TEMPLATE TO REACH

@app.route('/cssing')#
def cssing():
    return render_template("css.html")

@app.route('/csspassing/<color>/<othercolor>')#
def csspassing(color,othercolor):
    return render_template("csspassing.html",color =color, color2=othercolor)

@app.route('/csspassingtest/<color>/<othercolor>')#
def csspassingtest(color,othercolor):
    return render_template("csspassingtest.html",color =color, color2=othercolor)

























@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL'

if __name__ == "__main__":
    app.run(debug=True)#THIS WILL GIVE US PRINTOUT ERRORS IF THERE ARE ERRORS