from flask import Flask, redirect, request, json, send_file, make_response, render_template, url_for

import DataLoad
import KMeansKlasterService
import Aglomerative

app = Flask(__name__)


@app.route('/aglomerative/<filename>', methods=['GET', 'POST'])
def get_file(filename):
    Aglomerative.make_diagam(DataLoad.get_transformed_data(filename), 10)
    return render_template('kluster.html',
                           imgUrl3D='aglomerative3d.png',
                           imgUrl2D='aglomerative2d.png',
                           filename=filename)


@app.route('/aglomerative/pdf/<filename>', methods=['GET', 'POST'])
def get_agl_pdf(filename):
    pdf = Aglomerative.create_pdf(DataLoad.get_transformed_data(filename), 10)
    response = make_response(pdf)
    response.headers['Content-Disposition'] = "attachment; filename='police_stops_report.pdf"
    response.mimetype = 'application/pdf'
    return response


@app.route('/home', methods=['GET'])
def get_index():
    return render_template("index.html")


@app.route('/myfile', methods=['POST', 'GET'])
def get_myfile():
    filename = request.files['filz'].filename
    return render_template('methods.html', filename=filename)


@app.route('/getDefaultTestDataPredictions', methods=['GET'])
def get_default_test_predictions():
    return DataLoad.get_transformed_data().as_matrix()


@app.route('/loadData', methods=['POST'])
def load():
    data = json.loads(request.data)
    return data


@app.route('/kmeans/<filename>', methods=['GET', 'POST'])
def getDiagram(filename):
    KMeansKlasterService.make_diagam(5, filename)
    # send_file(img, mimetype='image/gif')
    return render_template('kluster.html',
                           imgUrl2D='kmeans2d.png',
                           filename=filename)


@app.route('/kmeans/pdf/<filename>', methods=['GET', 'POST'])
def getPdf(filename):
    pdf = KMeansKlasterService.create_pdf(5, filename)
    response = make_response(pdf)
    response.headers['Content-Disposition'] = "attachment; filename='police_stops_report.pdf"
    response.mimetype = 'application/pdf'
    return response
