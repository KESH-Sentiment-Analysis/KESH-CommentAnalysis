import pandas as pd


def data_separator(file_name, separation_percentage):
    # file_name = "../../data/corpus_sent.csv" для тестов, надо стереть file_name из начала функции чтобы тестить

    separation_percentage /= 100

    df = pd.read_csv(file_name, delimiter=',')  # читаю файл с примерами
    df = df.drop(['Unnamed: 0'], axis=1)  # убираю столбец с нумeрацией

    df = df.sample(frac=1).reset_index(drop=True)  # перемешиваю датафрейм

    # длины списков для тренировки и теста
    len_train = round(len(df) * separation_percentage)
    len_test = len(df) - len_train

    train = df.iloc[:len_train]
    test = df.iloc[len_train:len_test]

    return train, test
