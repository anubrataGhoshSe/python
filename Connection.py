import pymongo


class Connection:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["firstPyAPI"]
