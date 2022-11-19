import pymongo



client = pymongo.MongoClient("mongodb+srv://kevin_miner_test:Peerless123@cluster0.458zxp3.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)