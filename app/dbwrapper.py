import db
from flask import request

def getProduct(productId):
	obj = db.getProduct(productId)
	print obj
	return obj
	
def createProduct(productObj):
	print "Before extracting data"
	print "PRODUCT OBJECT:"+str(productObj)
	db.insertProduct(productObj)

def deleteProduct(productId):
	print 'before deleting'
	obj = db.deleteProduct(productId)
	return obj

def getAll(product_type):
	print 'getting all'
	products = db.getAll(product_type)
	return products