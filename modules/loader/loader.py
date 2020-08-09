"""
    Задача этого модуля -- загрузка данных
"""
import pandas as pd


def give_data(file_name, do_shuffle=True):
    # для тестов, надо стереть file_name из начала функции чтобы тестить
    # file_name = "../../data/corpus_sent.csv"

    # читаю файл с примерами
    df = pd.read_csv(file_name, delimiter=',')

    # убираю столбец с нумерацией
    df = df.drop(['Unnamed: 0'], axis=1)

    # перемешиваю датафрейм
    if do_shuffle:
        df = df.sample(frac=1).reset_index(drop=True)

    return df
