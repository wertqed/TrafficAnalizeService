from flask import Flask, request, json

app = Flask(__name__)


@app.route('/getDefaultTestDataPredictions', methods=['GET'])
def processing():
    return 'Test data prediction'


@app.route('/loadData', methods=['POST'])
def processing():
    data = json.loads(request.data)
    return data


