from flask import Flask , make_response, jsonify, render_template, request

import api
import json

app = Flask(__name__)

@app.route('/')
def get_index ():
   return render_template('index.html') 

@app.route('/sensor/api/v1.0/', methods = ['GET'])
def get_welcome():
    return (jsonify( { 'message':  "welcome"} ))

@app.route('/sensor/api/v1.0/clients', methods = ['GET'])
def get_clients():
    api.findClients () 
    return jsonify( api.resp )

@app.route('/sensor/api/v1.0/tags/<string:client>', methods = ['GET'])
def get_tags(client):
    api.findTags (client)
    return jsonify( api.resp )


@app.route('/sensor/api/v1.0/vals/<string:client>/tag/<string:tag>', methods = ['GET'])
def get_valsClientTag(client, tag):
    api.findValsClientTag (client, tag)
    return jsonify(api.resp)
   
@app.route('/sensor/api/v1.0/vals/minute/<string:client>/tag/<string:tag>', methods = ['GET'])
def get_valsMinuteClientTag(client, tag):
    api.findMinuteValsClientTag (client, tag)
    return  jsonify(api.resp)
 
@app.route('/sensor/api/v1.0/vals/hour/<string:client>/tag/<string:tag>', methods = ['GET'])
def get_valsHourClientTag(client, tag):
    api.findHourValsClientTag (client, tag)
    return jsonify(api.resp)

@app.route('/sensor/api/v1.0/vals/last/<string:client>/tag/<string:tag>', methods = ['GET'])
def get_LastValsClientTag(client, tag):
    api.findLastValsClientTag (client, tag)
    return jsonify(api.resp)



 
if __name__ == "__main__":
    app.run(debug=True)


