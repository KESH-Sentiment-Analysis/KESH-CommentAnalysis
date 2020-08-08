import pandas as pd


def data_separator(data_frame, separation_percentage):
    separation_percentage /= 100

    # длины списков для тренировки и теста
    len_train = round(len(data_frame) * separation_percentage)
    len_test = len(data_frame) - len_train

    train = data_frame.iloc[:len_train]
    test = data_frame.iloc[len_train:len_test]

    return train, test
