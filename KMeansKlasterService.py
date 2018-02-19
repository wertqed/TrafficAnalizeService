# -*- coding: utf-8 -*-
2
import subprocess

import DataLoad
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
import datetime
import io
import cStringIO
from reportlab.pdfgen import canvas
from mpl_toolkits.mplot3d import Axes3D


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


def make_diagam(count_klast, filename):
    data = DataLoad.get_transformed_data(filename).as_matrix()
    k_means = KMeans(n_clusters=count_klast, random_state=1)
    k_means.fit(data)
    centers = k_means.cluster_centers_
    print "silhuette:", metrics.silhouette_score(data, k_means.labels_)
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
    plt.savefig('static/kmeans2d.png')
    plt.show()
    plt.clf()

    # fig = plt.figure()
    # ax2 = Axes3D(fig)
    # ax2.scatter(data[:, 0], data[:, 1], data[:, 2], c=klusters, cmap='prism')
    # ax2.set_xlabel('driver_age')
    # ax2.set_ylabel('driver_gender')
    # ax2.set_zlabel('stop_time')
    # plt.savefig('static/kmeans3d.png')
    return img


def create_pdf(count_klast,filename):
    data = DataLoad.get_transformed_data(filename).as_matrix()
    k_means = KMeans(n_clusters=count_klast, random_state=1)
    k_means.fit(data)
    centers = k_means.cluster_centers_
    klusters = []
    for j in range(count_klast):
        klusters.append([])
    for i, la in enumerate(k_means.labels_):
        klusters[la].append(data[i])
    output = cStringIO.StringIO()
    p = canvas.Canvas(output)
    number = 1
    it = 1
    it2 = 1
    for k in klusters:
        if (800 - it * 20) < 20:
            it = 1
            it2 = 1
            p.showPage()
        it = it + 1
        it2 = it2 + 1
        p.drawString(100, 800 - it * 20, "center of klusters num" + str(number) + " age: " + str(
            int(centers[number - 1][0])) + " time: " + str(
            datetime.timedelta(seconds=int(centers[number - 1][2]))))
        it = it + 1
        it2 = it2 + 1
        p.drawString(50, 800 - it * 20, "Men")
        p.drawString(200, 800 - it * 20,  "Woman")
        it = it + 1
        it2 = it2 + 1
        for i in k:
            if (int(i[1]) == 0):
                if (800 - it * 20) < 20:
                    it = 1
                    it2 = 1
                    p.showPage()
                p.drawString(50, 800 - it * 20,
                             "age: " + str(int(i[0])) + " time: " + str(datetime.timedelta(seconds=int(i[2]))))
                it = it + 1
            else:
                if (800 - it2 * 20) < 20:
                    it = 1
                    it2 = 1
                    p.showPage()
                p.drawString(200, 800 - it2 * 20,
                             "age: " + str(int(i[0])) + " time: " + str(datetime.timedelta(seconds=int(i[2]))))
                it2 = it2 + 1
        number = number + 1

    p.save()
    pdf_out = output.getvalue()
    output.close()
    return pdf_out


make_diagam(50, "NC.csv")