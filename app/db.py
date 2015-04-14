from pymongo import MongoClient
from bson.json_util import dumps
URI =  "mongodb://adminuser:adminuser@ds059471.mongolab.com:59471/barcode"
client = MongoClient(URI)
db = client.get_default_database()

def insertProduct(productObj):
	product = db.product
	print "about to create object "+str(productObj)
	product.insert(productObj)
	return dumps({})
	#db.mynewcollection.insert({ "foo" : "bar" })

def getProduct(productId):
	product = db.product
	print "about to find product "+ str(productId)
	productObj = product.find_one({"code":productId})
	products = [productObj]
	for p in product.find({"type":productObj['type']}):
		if p['code']!=productObj['code']:
			products.append(p)

	return dumps(products)

def updateProduct(productObj):
	product = db.product
	product.find_one_and_update(productObj)

if __name__ == '__main__':
	main()