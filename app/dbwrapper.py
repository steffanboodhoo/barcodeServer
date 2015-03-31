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