import json


from flask import Flask, request
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/uplink', methods=['POST'])
def uplink_message():
    msg = request.get_json()
    json_data = json.dumps(msg)
    print(json_data)
    return "uplink message successful"


@app.route('/response', methods=['GET'])
def get_response():
    return "Hurray"


@app.route('/', methods=['GET'])
def default():
    return "Default method accessed"