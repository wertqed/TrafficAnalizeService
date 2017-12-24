# -*- coding: utf-8 -*-
from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import DataLoad
from scipy.cluster.hierarchy import fcluster, cophenet
from sklearn import metrics
from sklearn import preprocessing

from sklearn.cluster import AgglomerativeClustering

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
    # plt.show()

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
        num_lables[label]+=1
    klust_sizes = []
    for i in range(n_clusters):
        legend.append('num:' + str(num_lables[i]))
        klust_sizes.append(num_lables[i])
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.title('Size of klasters', size=14)
    plt.pie(klust_sizes,
            labels=num_lables)
    fig = plt.figure()

    distance_mat = pdist(data) # pdist посчитает нам верхний треугольник матрицы попарных расстояний
    Z = hierarchy.linkage(distance_mat, 'ward') # linkage — реализация агломеративного алгоритма
    clusters = fcluster(Z, 0.9, criterion='distance')
    ax = Axes3D(fig)
    ax.scatter(data[:, 0], data[:, 1], data[:,2], c=labels, cmap='prism')
    ax.set_xlabel('driver_age')
    ax.set_ylabel('driver_gender')
    ax.set_zlabel('stop_time')
    plt.show()
    # img = io.BytesIO()
    # plt.savefig(img, format='png')
    # return img

make_diagam(DataLoad.get_transformed_data(), 10)