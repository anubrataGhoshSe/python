from Connection import Connection
from bson.json_util import dumps


def createone(collection, obj):
    conn = Connection()
    mycol = conn.mydb[collection]
    mycol.insert_one(obj)
    cursor = mycol.find()
    list_cur = list(cursor)
    json_dumps = dumps(list_cur)
    print("from repo createOne(): ", json_dumps)

    return json_dumps
