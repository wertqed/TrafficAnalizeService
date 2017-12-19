# -*- coding: utf-8 -*-
import numpy as np
from pandas import read_csv
from sklearn.cluster import KMeans
import datetime


def get_csv_data():
    dataframe = read_csv('NC.csv', engine='python', nrows=1000)
    print len(dataframe)
    data = dataframe.loc[(dataframe['driver_age']) > 0 & np.isnan(dataframe['driver_gender'] == False) & np.isnan(
        ['stop_time'] == False)]
    return data[['driver_age', 'driver_gender', 'stop_time']]


def sex_to_bool(sex):
    if sex == "M":
        return 0
    return 1


def time_to_seconds(time):
    return datetime.timedelta(hours=float(time[0:2]), minutes=float(time[3:5])).seconds


def get_transformed_data():
    data = get_csv_data()
    data['driver_gender'] = data['driver_gender'].apply(sex_to_bool)
    data['stop_time'] = data['stop_time'].apply(time_to_seconds)
    return data


print get_transformed_data()

# data = self.data.loc[self.data['Number of speakers'] < 100]
# data_for_cl = self.data[['Number of speakers', 'Latitude', 'Longitude']].as_matrix()
# data_for_ll = self.data[['Latitude', 'Longitude']].as_matrix()

# k_means = KMeans(n_clusters=8)
# a = k_means.fit(data)
# centrx = k_means.cluster_centers_

# print centrx
