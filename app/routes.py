from app import flaskapp
from flask import render_template
from flask import request
from flask import jsonify
import ast
import json
import dbwrapper

@flaskapp.route('/')
@flaskapp.route('/home')
def index():
    return render_template('home.html')

@flaskapp.route('/adduser')
def signIn():
    return render_template('adduser.html')

@flaskapp.route('/registration')
def registration():
    return render_template('RegistrationPage.html')


@flaskapp.route('/newproduct',methods=['GET','POST'])
def newproduct():
	json_str=u''+str(request.get_data())
	print json_str
	productObj = json.loads(json_str)
	obj = dbwrapper.createProduct(productObj)
	return obj

@flaskapp.route('/getproduct/<int:product_id>')
def getproduct(product_id):
	obj = dbwrapper.getProduct(product_id)
	print obj
	return obj

@flaskapp.route('/deleteproduct/<int:product_id>',methods=['DELETE'])
def deleteproduct(product_id):
	obj = dbwrapper.deleteProduct(product_id)
	print obj
	return obj


@flaskapp.route('/getall/<string:product_type>')
def getAll(product_type):
	print 'hellooooooo'
	obj = dbwrapper.getAll(product_type)
	print obj
	return obj


@flaskapp.route('/validateuser/<string:username>/<string:password>')
def validateUser(username,password):
	print 'about to validateuser'
	'''
	json_str=u''+str(request.get_data())
	print json_str
	managerObj = json.loads(json_str)
	'''
	resp = dbwrapper.validateuser(username,password)
	return resp

@flaskapp.route('/getmanagers',methods=['GET','OPTIONS'])
def getManagers():
	resp = dbwrapper.getManagers()
	return resp

@flaskapp.route('/newmanager',methods=['GET','POST','OPTIONS'])
def newmanager():
	json_str=u''+str(request.get_data())
	print json_str
	ManagerObj = json.loads(json_str)
	obj = dbwrapper.createManager(ManagerObj)
	return obj