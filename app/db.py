from pymongo import MongoClient
URI =  mongodb://adminuser:adminuser@ds059471.mongolab.com:59471/barcode
client = MongoClient(URI)
db = client.get_default_database()

def insertProduct(productObj):
	product = db.product
	product.insert(productObj)

def getProduct(productId):
	product = db.product
	productObj = product.find_one({"_id":productId})
	return productObj

def updateProduct(productObj):
	product = db.product
	product.find_one_and_update(productObj)

if __name__ == '__main__':
	main()