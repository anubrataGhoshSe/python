from Connection import Connection
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
