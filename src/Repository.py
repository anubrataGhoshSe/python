from pymongo import ReturnDocument

from src.Connection import Connection
from bson.json_util import dumps
from bson.objectid import ObjectId

def createOne(collection, obj):
    conn = Connection()
    mycol = conn.mydb[collection]
    mycol.insert_one(obj)
    cursor = mycol.find()
    list_cur = list(cursor)
    json_dumps = dumps(list_cur)
    print("from repo createOne(): ", json_dumps)

    return json_dumps

def createOne(collection, obj, fileName):
    conn = Connection()
    mycol = conn.mydb[collection]
    mycol.insert_one(obj)
    cursor = mycol.find({"fileName": fileName})
    list_cur = list(cursor)
    json_dumps = dumps(list_cur)
    print("from repo createOne(): ", json_dumps)

    return json_dumps


def updateOne(collection, query, newvalue):
    conn = Connection()
    mycol = conn.mydb[collection]
    mycol.update_one(query, newvalue)
    cursor = mycol.find()
    list_cur = list(cursor)
    json_dumps = dumps(list_cur)
    print("updated collection: ", json_dumps)
    return json_dumps


def findAll(collection):
    conn = Connection()
    mycol = conn.mydb[collection]
    cursor = mycol.find()
    list_cur = list(cursor)
    json_dumps = dumps(list_cur)
    return json_dumps


def deleteOne(collection, _id):
    conn = Connection()
    mycol = conn.mydb[collection]
    mycol.delete_one({"_id": ObjectId(_id)})
    obj = mycol.find()
    _json = dumps(list(obj))
    return _json


def isExist(collection, query):
    conn = Connection()
    mycol = conn.mydb[collection]
    print("Repo -> isExist -> collection: ",collection, "query: ", query)
    lst = list(mycol.find(query))
    if len(lst) > 0:
        return "true"
    else:
        return "false"


def findAndUpdate(collection, findquery, updatewith):
    print("Repository -> findquery: ", findquery)
    print("Repository -> updatewith: ", updatewith)
    conn = Connection()
    mycol = conn.mydb[collection]
    mycol.find_one_and_update(findquery, {'$set': updatewith})

    __json = findone(collection, findquery)
    print("__json: ", __json)
    return __json
    #return mycol.find_one_and_update(findquery, {'$set': updatewith}, return_document=ReturnDocument.AFTER)

def findone(collection, payload):
    print("Repo->findone->collection: ", collection)
    print("Repo->findone->payload: ", payload)
    conn = Connection()
    mycol = conn.mydb[collection]
    cursor = mycol.find(payload)
    __json = dumps(list(cursor))
    return __json

