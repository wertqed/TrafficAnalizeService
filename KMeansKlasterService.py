# -*- coding: utf-8 -*-
import DataLoad
from sklearn.cluster import KMeans
from sklearn import metrics


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


def check_kluster(data):
    klusters = get_klasters(8)


get_klasters(2)
