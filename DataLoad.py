# -*- coding: utf-8 -*-
import numpy as np
from pandas import read_csv
import datetime


# Загрузка из CSV файла
def get_csv_data():
    dataframe = read_csv('NC.csv', engine='python', nrows=1000).dropna(subset=['driver_age', 'driver_gender', 'stop_time'])
    data = dataframe.loc[(dataframe['driver_age']) > 0]
    data = data[['driver_age', 'driver_gender', 'stop_time']]
    return data

def sex_to_bool(sex):
    if sex == "M":
        return 0
    return 1


def time_to_seconds(time):
    return datetime.timedelta(hours=float(time[0:2]), minutes=float(time[3:5])).seconds


# получение преобразованных данных
def get_transformed_data():
    data = get_csv_data()
    data['driver_gender'] = data['driver_gender'].apply(sex_to_bool)
    data['stop_time'] = data['stop_time'].apply(time_to_seconds)
    return data
