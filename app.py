#!/bin/python

#Flask application for getting data and creating an api
#install flask using pip3: pip3 install flask

from flask_bootstrap import Bootstrap
from flask import Flask ,render_template
app= Flask(__name__)
bootstrap = Bootstrap(app)

#in python we can name by using __my__grade = 90
#index home page
@app.route("/")
def index():
    return render_template('index.html')

#sign up page
@app.route('/SignUp')
def SignUp():
    return render_template('sign_up.html')

#login page
@app.route('/SignIn')
def SignIn():
    return render_template('sign_in.html')

#users page
@app.route('/Users')
def Users():
    return render_template('users.html')


def hello():
    return "hello lucia"


def my_name():
    return "my name is lucia mutuku"


if __name__ == "__main__":
    app.run()

