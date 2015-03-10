from app import flaskapp
from flask import render_template
@flaskapp.route('/')
@flaskapp.route('/home')
def index():
    return render_template('home.html')

@flaskapp.route('/signIn')
def signIn():
    return render_template('Signin.html')

@flaskapp.route('/registration')
def registration():
    return render_template('RegistrationPage.html')
