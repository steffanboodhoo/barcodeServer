from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.barcodes

def insertProduct(productObj):
	product = db.product
	product.insert(productObj)

def getProduct(productId):
	product = db.product
	productObj = product.find_one("_id":productId)
	return productObj

def updateProduct(productObj):
	product = db.product
	product.find_one_and_update(productObj)

if __name__ == '__main__':
	main()