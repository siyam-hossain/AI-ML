from flask import Flask, render_template, request
# request is used for GET POST methods

'''
It creates an instance of the Flask class, which will be your WSGI (Web Server GateWay Interface) application.
'''
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>Welcome to Flask</h1>"

# by default route contain important method called GET
# route(str, method=["GET"])
@app.route("/index", methods=['GET'])
def redirect():
    return render_template('002-index.html')

@app.route("/about")
def about():
    return render_template('002-about.html')

# GET POST 
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subjects = request.form['subjects']
        message = request.form['message']

        return f"Name: {name}\nEmail: {email}\nSubject: {subjects}\nMessage: {message}"

    return render_template('003-form.html')




# entry point
if __name__ == "__main__":

    app.run(debug=True) 


# to run the server
# python 018-Flask-Framework/002-flask-skeleton/flask/003-get-post.py