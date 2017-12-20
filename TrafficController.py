from flask import Flask, request, json, send_file, make_response
import DataLoad
import KMeansKlasterService

app = Flask(__name__)


@app.route('/getDefaultTestDataPredictions', methods=['GET'])
def get_default_test_predictions():
    return DataLoad.get_transformed_data().as_matrix()


@app.route('/loadData', methods=['POST'])
def load():
    data = json.loads(request.data)
    return data


@app.route('/getDiagram', methods=['GET'])
def getDiagram():
    img = KMeansKlasterService.make_diagam(5)
    response = make_response(img.getvalue())
    response.headers['Content-Type'] = 'image/png'
    # send_file(img, mimetype='image/gif')
    return response
