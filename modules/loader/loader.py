"""
    Задача этого модуля -- загрузка данных
"""

# импортируй здесь нужные тебе библиотеки
# from ... import ...
import pandas as pd


def load_data():
    """Ваш код тут"""


def give_data(file_name):
    # file_name = "../../data/corpus_sent.csv" #для тестов, надо стереть file_name из начала функции чтобы тестить
    df = pd.read_csv(file_name, delimiter=',')  # читаю файл с примерами
    df = df.drop(['Unnamed: 0'], axis=1)  # убираю столбец с нумирацией
    data_frame = df.sample(frac=1).reset_index(drop=True)  # перемешиваю датафрейм
    return data_frame
