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
  		db.insertProduct(productObj)
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