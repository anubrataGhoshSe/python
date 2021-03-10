import Repository


def createcountry(payload):
    obj = Repository.createone("country", payload)
    return obj
