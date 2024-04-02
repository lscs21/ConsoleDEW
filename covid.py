import numpy as np
import pandas as pd
import math


def getAvailableCountries():
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/total_cases.csv'
    dataset = pd.read_csv(url, sep=',', parse_dates=True)
    
    countries = list(dataset.columns[2:])
    return countries

def _turnNanIntoZero(value):
    if (math.isnan(value)):
        return 0
    return value

def getFirstValidIndex(array):
    iterator = 0
    while(array[iterator] == 0):
        iterator = iterator+1
    return iterator

def getCovidData(countryName='World', dataType='total_cases'):
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/'+dataType+'.csv'
    dataset = pd.read_csv(url, parse_dates=True)
    cols = ['date', countryName]

    filtered_dataset = dataset[cols].values
    iterator = 0
    date_results = np.empty(len(filtered_dataset),dtype='<U10')
    count_results = np.empty(len(filtered_dataset), dtype='int')

    for row in filtered_dataset:
        date_results[iterator] = str(row[0])
        count_results[iterator] = _turnNanIntoZero(row[1])
        iterator = iterator + 1

    return count_results, date_results

def getData(FileName):
    DataName = 'Files/Dataset/' + FileName
    dataset = pd.read_csv(DataName, sep=',', parse_dates=True)

    cols = ['date', 'totalcases']

    #filtered_dataset = dataset[cols].values
    filtered_dataset = dataset.values
    
    iterator = 0
    date_results = np.empty(len(filtered_dataset),dtype='<U10')
    count_results = np.empty(len(filtered_dataset), dtype='int')

    for row in filtered_dataset:
        date_results[iterator] = str(row[0])
        count_results[iterator] = _turnNanIntoZero(row[1])
        iterator = iterator + 1

    return count_results, date_results