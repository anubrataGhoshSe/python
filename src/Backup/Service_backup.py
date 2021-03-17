from src import Repository
from bson.objectid import ObjectId


def createCountry(payload):
    obj = Repository.createOne("country", payload)
    return obj


def updateCountry(payload):
    _id = payload.get("_id")
    query = {"_id": ObjectId(_id)}
    print("query: ", query)
    newvalue = {"$set": payload.get("data")}
    print("newvalue", newvalue)
    obj = Repository.updateOne("country", query, newvalue)
    return obj


def deleteCountry(_id):
    return Repository.deleteOne("country", _id)


def findAll(collection):
    return Repository.findAll(collection)
