import db
from flask import request

def getProduct(productId):
	obj = db.getProduct(productId)
	print obj
	if obj is None:
		return ""
	return obj
	
def createProduct(requestObj):
	productObj = {"id":requestObj.form['id'],
				"name":requestObj.form['name']}
	print "PRODUCT OBJECT:"+str(productObj.name)
	db.insertProduct(productObj)