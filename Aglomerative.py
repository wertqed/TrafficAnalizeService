# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import metrics
from sklearn import preprocessing
import io
import cStringIO
from reportlab.pdfgen import canvas
import datetime
from sklearn.cluster import AgglomerativeClustering

import DataLoad


def doAgglomerative(data, n_clusters):
    minmax_scale = preprocessing.MaxAbsScaler().fit(data)
    data = minmax_scale.transform(data)
    clustering = AgglomerativeClustering(linkage='ward', n_clusters=n_clusters)
    labels = clustering.fit_predict(data)
    # distance_mat = pdist(data) # pdist посчитает нам верхний треугольник матрицы попарных расстояний
    # Z = hierarchy.linkag9e(distance_mat, 'ward') # linkage — реализация агломеративного алгоритма
    # clusters = fcluster(Z, 0.9, criterion='distance')
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # ax.scatter(data[:, 0], data[:, 1], data[:,2], c=labels, cmap='prism')
    # ax.scatter(data['driver_age'], data['driver_gender'], data['stop_time'], c=clusters, cmap='prism')
    # ax.set_xlabel('driver_age')
    # ax.set_ylabel('driver_gender')
    # ax.set_zlabel('stop_time')
    # dn = hierarchy.dendrogram(Z, color_threshold=0.05)
    print metrics.silhouette_score(data, labels=labels)


def make_diagam(data, n_clusters):
    minmax_scale = preprocessing.MaxAbsScaler().fit(data)
    data = minmax_scale.transform(data)
    clustering = AgglomerativeClustering(linkage='ward', n_clusters=n_clusters)
    labels = clustering.fit_predict(data)
    legend = []
    num_lables = []
    for i in range(n_clusters):
        num_lables.append(0)
    for label in labels:
        num_lables[label] += 1
    klust_sizes = []
    for i in range(n_clusters):
        legend.append('num:' + str(num_lables[i]))
        klust_sizes.append(num_lables[i])
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.pie(klust_sizes,
            labels=num_lables)

    plt.savefig('static/aglomerative2d.png')
    fig = plt.figure()
    ax2 = Axes3D(fig)
    ax2.scatter(data[:, 0], data[:, 1], data[:, 2], c=labels, cmap='prism')
    ax2.set_xlabel('driver_age')
    ax2.set_ylabel('driver_gender')
    ax2.set_zlabel('stop_time')
    plt.savefig('static/aglomerative3d.png')

def create_pdf(data, n_clusters):
    tmp = data.as_matrix()
    minmax_scale = preprocessing.MaxAbsScaler().fit(data)
    data = minmax_scale.transform(data)
    clustering = AgglomerativeClustering(linkage='ward', n_clusters=n_clusters)
    labels = clustering.fit_predict(data)
    legend = []
    num_lables = []
    for i in range(n_clusters):
        num_lables.append(0)
    for label in labels:
        num_lables[label] += 1
    klust_sizes = []
    for i in range(n_clusters):
        legend.append('num:' + str(num_lables[i]))
        klust_sizes.append(num_lables[i])
    output = cStringIO.StringIO()
    p = canvas.Canvas(output)
    number = 1
    it = 1
    it2 = 1
    for j in range(n_clusters):
        if (800 - it * 20) < 20:
            it = 1
            it2 = 1
            p.showPage()
        it = it + 1
        it2 = it2 + 1
        p.drawString(100, 800 - it * 20, "cluster " + str(j + 1))
        it = it + 1
        it2 = it2 + 1
        p.drawString(50, 800 - it * 20, "Men")
        p.drawString(200, 800 - it * 20, "Woman")
        it = it + 1
        it2 = it2 + 1
        for i in range(len(tmp)):
            if(labels[i] == j) :
                if (int(tmp[i][1]) < 1):
                    if (800 - it * 20) < 20:
                        it = 1
                        it2 = 1
                        p.showPage()
                    p.drawString(50, 800 - it * 20,
                                 "age: " + str(int(tmp[i][0])) + " time: " + str(datetime.timedelta(seconds=int(tmp[i][2]))))
                    it = it + 1
                else:
                    if (800 - it2 * 20) < 20:
                        it = 1
                        it2 = 1
                        p.showPage()
                    p.drawString(200, 800 - it2 * 20,
                                 "age: " + str(int(tmp[i][0])) + " time: " + str(datetime.timedelta(seconds=int(tmp[i][2]))))
                    it2 = it2 + 1

    p.save()
    pdf_out = output.getvalue()
    output.close()
    return pdf_out

# doAgglomerative(DataLoad.get_transformed_data('10000.csv'), 10)