import db
from flask import request
from bson.json_util import dumps

def getProduct(productId):
	obj = db.getProduct(productId)
	print obj
	return obj
	
def createProduct(productObj):
	print "Before extracting data"
	print "PRODUCT OBJECT:"+str(productObj)
	try:
  		obj = db.insertProduct(productObj)
  		return obj
	except Exception: 
		return dumps({'status':'failure'})
	

def deleteProduct(productId):
	print 'before deleting'
	obj = db.deleteProduct(productId)
	return obj

def getAll(product_type):
	print 'getting all'
	products = db.getAll(product_type)
	return products

def validateuser(username,password):
	#print 'inside wrapper'
	#password = user.password
	#username = user.username
	print username,password
	resp = db.checkPassword(username,password)
	return resp