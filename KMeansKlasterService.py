# -*- coding: utf-8 -*-
import DataLoad
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
import datetime
import io
import cStringIO
from reportlab.pdfgen import canvas


def get_k_means(count_klast):
    data = DataLoad.get_transformed_data().as_matrix()
    k_means = KMeans(n_clusters=count_klast)
    fits = k_means.fit(data)
    return k_means


def get_klasters(count_klast):
    data = DataLoad.get_transformed_data().as_matrix()
    k_means = KMeans(n_clusters=count_klast)
    fits = k_means.fit(data)
    centrx = k_means.cluster_centers_
    klusters = []
    for j in range(count_klast):
        klusters.append([])
    for i, la in enumerate(k_means.labels_):
        klusters[la].append(data[i])
    print "silhuette:", metrics.silhouette_score(data, k_means.labels_)
    return klusters


def make_diagam(count_klast):
    data = DataLoad.get_transformed_data().as_matrix()
    k_means = KMeans(n_clusters=count_klast, random_state=1)
    k_means.fit(data)
    centers = k_means.cluster_centers_
    klusters = []
    for j in range(count_klast):
        klusters.append([])
    for i, la in enumerate(k_means.labels_):
        klusters[la].append(data[i])
    # Создание легенды
    legend = []
    for center in centers:
        legend.append('age:' + str(int(center[0])) + '\ntime ' + str(datetime.timedelta(seconds=int(center[2]))))
    # Делаем данные для графика
    klust_sizes = []
    for kluster in klusters:
        klust_sizes.append(len(kluster))
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.title('Size of klasters', size=14)
    plt.pie(klust_sizes,
            labels=legend)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.clf()
    return img


def create_pdf(count_klast):
    data = DataLoad.get_transformed_data().as_matrix()
    k_means = KMeans(n_clusters=count_klast, random_state=1)
    k_means.fit(data)
    centers = k_means.cluster_centers_
    klusters = []
    for j in range(count_klast):
        klusters.append([])
    for i, la in enumerate(k_means.labels_):
        klusters[la].append(data[i])

    colors = ['black', 'green', 'yellow', 'blue', 'fuchsia', 'red', 'indigo', 'cyan']
    output = cStringIO.StringIO()
    p = canvas.Canvas(output)
    p.save()
    pdf_out = output.getvalue()
    output.close()
    return pdf_out
