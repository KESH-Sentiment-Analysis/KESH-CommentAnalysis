import numpy as np
import pandas as pd


def data_separator():
    file_name = 'corpus_sent.csv'
    df = pd.read_csv(file_name, delimiter=',')  # читаю файл с примерами
    df = df.drop(['Unnamed: 0'], axis=1)  # убираю столбец с нумирацией
    train = df.iloc[:25816]
    test = df.iloc[25816:32272]
    return train, test


data_separator()
