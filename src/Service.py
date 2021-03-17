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


def findAndUpdate(collection, payload):
    print("Service -> payload: ", payload)
    findQuery = payload['searchPayload']
    updateWith = payload['updatewithPayload']

    lst = Repository.findAndUpdate(collection, findQuery, updateWith)
    if lst is not None and len(lst) > 0:
        return lst
    else:
        return []


def isExist(collection, query):
    return Repository.isExist(collection, query)


def createOne(collection, obj):
    return Repository.createOne(collection, obj)


def trackOne(collection, obj):
    return Repository.createOne(collection, obj, obj['fileName'])


def findone(collection, payload):
    return Repository.findone(collection, payload)
