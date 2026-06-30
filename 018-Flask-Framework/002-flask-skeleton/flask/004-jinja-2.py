from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>Welcome to Flask</h1>"


@app.route("/index", methods=['GET'])
def index():
    return render_template('002-index.html')


@app.route("/about")
def about():
    return render_template('002-about.html')


# Contact Form
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subjects = request.form['subjects']
        message = request.form['message']

        return f"""
        Name: {name}<br>
        Email: {email}<br>
        Subject: {subjects}<br>
        Message: {message}
        """

    return render_template('004-submit.html')


@app.route('/success/<int:score>')
def success(score):
    res = ""

    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    return render_template('004-result.html', result=res)


@app.route('/success_res/<int:score>')
def result_exp(score):

    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {
        'score': score,
        'res': res
    }

    return render_template('004-result-exp.html', results=exp)


@app.route('/success_if/<int:score>')
def success_if(score):
    return render_template('004-result.html', results=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('004-result.html', results=score)


@app.route('/submit-subject')
def submit_subject():
    return render_template('004-get-result.html')


# Marks Form
@app.route('/submit_t', methods=['GET', 'POST'])
def submit_t():
    print(request.method)

    total_score = 0

    if request.method == 'POST':
        print(request.form)

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = science + maths + c + data_science

        print(total_score)

    return redirect(url_for('result_exp', score=int(total_score)))


if __name__ == "__main__":
    app.run(debug=True)