import db
from flask import request

def getProduct(productId):
	obj = db.getProduct(productId)
	print obj
	if obj is None:
		return ""
	return obj
	
def createProduct(productObj):
	print "Before extracting data"
	print "PRODUCT OBJECT:"+str(productObj)
	db.insertProduct(productObj)