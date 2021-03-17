from flask import Flask, jsonify, request, render_template
from src import Service
from flask_cors import CORS
from bson.json_util import dumps


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


countries = [{'id': 1, 'name': "INDIA"},
           {'id': 2, 'name': "UK"},
           {'id': 3, 'name': "USA"}]


@app.route('/')
def index():
    #return "welcome"
    return render_template("index.html")



@app.route( '/countries', methods=['GET'])
def getAllCountries():
    return jsonify({'countries': countries})


@app.route('/countries/<int:id>', methods=['GET'])
def getCountryById(id):
    return jsonify({'country': [obj for obj in countries if obj['id']==id]})


@app.route('/getRequestQueryParams', methods=['GET'])
def getRequestQueryParams():
    reqIds = request.args.get('ids')
    reqNames = request.args.get('name')
    print("reqIds: ", reqIds)
    print("reqNames: ", reqNames)
    return jsonify({'reqIds': reqIds,'reqNames':reqNames})


@app.route('/getCountryByIds', methods=['GET'])
def getCountryByIds():
    reqIds = request.args.get('ids').split(",")
    print("reqIds array: ", reqIds)
    resobj = []
    for id in reqIds:
        print(id)
        for country in countries:
            if country.get('id') == int(id):
                print("countryObj", country)
                resobj.append(country)
    print("requested countries: ", resobj)
    return jsonify({'countries_by_id': resobj})


@app.route("/sendPayload", methods=['POST'])
def sendPayload():
    payload = request.json
    print("payload: ", payload)
    return jsonify({"payload": payload})


@app.route("/updateJsonById", methods=['POST', 'PUT'])
def updateJsonById():
    payload = request.json
    print("payload: ", payload)

    reqHeaders = request.headers
    print("reqHeaders: ", reqHeaders)
    print("token: ", reqHeaders.get('token'))

    updatingIds = payload.get("ids")
    print("updatingIds: ", updatingIds)
    for id in updatingIds:
        for country in countries:
            if country['id'] == id:
                existingobj = country
                desc = {"description": payload.get('desc')}
                existingobj.update(desc)

    print("Final updated JSON: ", countries)
    return jsonify({"countries": countries})


@app.route('/insertCountry', methods=['POST'])
def insertCountry():
    payload = request.json
    print("update country payload: ", payload)
    obj = Service.createCountry(payload)
    print("obj: ", obj)
    return obj


@app.route("/updateCountry", methods=['POST'])
def updateCountry():
    obj = Service.updateCountry(request.json)
    return obj


@app.route("/getAllCountry", methods=['GET'])
def getAllCountry():
    return Service.findAll("country")


@app.route('/delCountry/<id>', methods=['POST', 'DELETE'])
def delCountry(id):
    return Service.deleteCountry(str(id))


@app.route('/api/filetrack', methods=['POST'])
def filetracking():
    #{'search':{'fileName': 'demo'}, 'hash': ''}
    #json = request.form
    requestpayload = request.json
    print("requestpayload: ", requestpayload)
    searchPayload = requestpayload['search']
    print("searchPayload: ", searchPayload)
    hash = requestpayload['hash']
    print("hash: ", hash)
    print("isExist: ", Service.isExist("trackingFileChange", searchPayload))
    if Service.isExist("trackingFileChange", searchPayload) == 'true':
        if hash != "":
            updatewithPayload = {"hash": hash}
            sendPayload = {'searchPayload': searchPayload, 'updatewithPayload': updatewithPayload}
            status = Service.findAndUpdate('trackingFileChange', sendPayload)
            __json = dumps(status)
            print("status: ", __json)
            return __json
        else:
            existingHash = Service.findone("trackingFileChange", searchPayload)
            print("filetracking->existingHash: ", existingHash)
            return existingHash
    else:
        status = Service.trackOne('trackingFileChange', {'fileName': searchPayload['fileName'], 'hash': requestpayload['hash']})
        return status


@app.route('/api/filetrackAJAX', methods=['POST'])
def filetrackAJAX():
    #{'search':{'fileName': 'demo'}, 'hash': ''}
    #json = request.form
    fileName = request.form['fileName']
    print("fileName: ", fileName)
    hash = request.form['hash']
    print("hash: ", hash)
    searchPayload = {"fileName": fileName}
    print("isExist: ", Service.isExist("trackingFileChange", searchPayload))
    if Service.isExist("trackingFileChange", searchPayload) == 'true':
        if hash != "":
            updatewithPayload = {"hash": hash}
            sendPayload = {'searchPayload': searchPayload, 'updatewithPayload': updatewithPayload}

            status = Service.findAndUpdate('trackingFileChange', sendPayload)
            #__json = dumps(status)
            return status
        else:
            existingHash = Service.findone("trackingFileChange", searchPayload)
            print("filetrackAJAX->existingHash: ", existingHash)
            return existingHash
    else:
        status = Service.trackOne('trackingFileChange', {'fileName': fileName, 'hash': hash})
        return status
@app.route('/api/findhashByFileName', methods=['POST'])
def findhashByFileName():
    fileName = request.form['fileName']
    print("findhashByFileName->fileName: ", fileName)
    existingHash = Service.findone("trackingFileChange", {"fileName": fileName})
    print("findhashByFileName->existingHash: ", existingHash)
    return existingHash


@app.route('/demo')
def demo():
    return render_template("demo.html")


@app.route('/demo1')
def demo1():
    return render_template("demo1.html")


if __name__ == "__main__":
    app.run(debug=True)
