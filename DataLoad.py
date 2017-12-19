# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import datetime, time


def get_csv_data():
    dataframe = read_csv('NC.csv', engine='python', nrows=1000)
    print len(dataframe)
    data = dataframe.loc[(dataframe['driver_age']) > 0 & np.isnan(dataframe['driver_gender'] == False) & np.isnan(
        ['stop_time'] == False)]
    return data[['driver_age', 'driver_gender', 'stop_time']].as_matrix()


print get_csv_data()

# data = self.data.loc[self.data['Number of speakers'] < 100]
# data_for_cl = self.data[['Number of speakers', 'Latitude', 'Longitude']].as_matrix()
# data_for_ll = self.data[['Latitude', 'Longitude']].as_matrix()
# k_means = KMeans(n_clusters=8)
# a = k_means.fit(data_for_cl)
# centrx = k_means.cluster_centers_
