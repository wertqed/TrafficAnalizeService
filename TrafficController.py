from flask import Flask, request, json
import DataLoad
app = Flask(__name__)


@app.route('/getDefaultTestDataPredictions', methods=['GET'])
def get_default_test_predictions():
    return DataLoad.get_transformed_data().as_matrix()


@app.route('/loadData', methods=['POST'])
def load():
    data = json.loads(request.data)
    return data


