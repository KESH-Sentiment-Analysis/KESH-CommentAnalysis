import numpy as np
import pandas as pd


def data_separator(file_name, separation_percentage):
    separation_percentage /= 100
    # file_name = "../../data/corpus_sent.csv" для тестов, надо стереть file_name из начала функции чтобы тестить
    df = pd.read_csv(file_name, delimiter=',')  # читаю файл с примерами
    df = df.drop(['Unnamed: 0'], axis=1)  # убираю столбец с нумирацией
    df = df.sample(frac=1).reset_index(drop=True)  # перемешиваю датафрейм
    len_train = round(len(df) * separation_percentage)  # Длина тренировочного списка
    len_test = len(df) - len_train  # Длина тестировочного списка
    train = df.iloc[:len_train]
    test = df.iloc[len_train:len_test]
    return train, test
