from flask import Flask, redirect, request, json, send_file, make_response, render_template, url_for

import DataLoad
import KMeansKlasterService

app = Flask(__name__)


@app.route('/getAglomerative', methods=['GET', 'POST'])
def get_file():
    return render_template('kluster.html',
                           imgUrl3D='aglomerative3d.png',
                           imgUrl2D='aglomerative2d.png',
                           type='aglomerative')


@app.route('/home', methods=['GET'])
def get_index():
    if request.method == 'POST':
        return redirect('/choosemethod')
    else:
        return render_template("index.html")


@app.route('/myfile', methods=['POST', 'GET'])
def get_myfile():
    if request.method == 'POST':
        return redirect(url_for('get_method'))


@app.route('/choosemethod', methods=['GET', 'POST'])
def get_method():
    return render_template('file.html')


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


@app.route('/getPdf', methods=['GET'])
def getPdf():
    pdf = KMeansKlasterService.create_pdf(5)
    response = make_response(pdf)
    response.headers['Content-Disposition'] = "attachment; filename='police_stops_report.pdf"
    response.mimetype = 'application/pdf'
    return response