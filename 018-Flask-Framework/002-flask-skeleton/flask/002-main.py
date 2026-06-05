from flask import Flask, render_template

# render template: is responsible for redirecting something like html page

'''
It creates an instance of the Flask class, which will be your WSGI (Web Server GateWay Interface) application.
'''
app = Flask(__name__)


# create basic route 
# decorator:  
@app.route("/")
def welcome():
    return "<h1>Welcome to Flask</h1>"

# redirecting here
# first it will find directory called templates
# then find 002-index.html
@app.route("/index")
def redirect():
    return render_template('002-index.html')

@app.route("/about")
def about():
    return render_template('002-about.html')


# entry point
if __name__ == "__main__":

    app.run(debug=True) 



# to run the server
# python 018-Flask-Framework/002-flask-skeleton/flask/002-main.py