from app import flaskapp
from flask import render_template
from flask import request
import json
import dbwrapper

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

@flaskapp.route('/newproduct',methods=['GET','POST'])
def newproduct():
	json_str=u''+str(request.get_data())
	print json_str
	productObj = json.loads(json_str)
	dbwrapper.createProduct(productObj)
	return "something"

@flaskapp.route('/getproduct/<int:product_id>')
def getproduct(product_id):
	return dbwrapper.getProduct(product_id)
	

