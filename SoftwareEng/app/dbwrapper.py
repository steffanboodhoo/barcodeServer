import db
from flask import request

def getProduct(requestObj):
	productId = request.args.get('productId')
	obj = db.getProduct(productId)
	if obj is None:
		return "no object found"
	return obj
	
def createProduct(requestObj):
	product = requestObj.args.get('product')
	db.insertProduct(productObj)