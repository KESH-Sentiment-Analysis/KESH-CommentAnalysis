"""
    Задача этого модуля -- обучение модели
"""

from sklearn import svm
from modules.fitter.validator import validator
from modules.fitter.evaluation import evaluate_model

import pickle as pk


def fit_model(X_train, Y_train, X_test, Y_test):
    C, kernel = validator(X_train, Y_train)  # получение необходимых параметров
    model = svm.SVC(kernel=kernel, C=C)  # модель принимает необходимые параметры
    model.fit(X_train, Y_train)  # модель обучается на тренировочных данных
    y_predict = model.predict(
        X_test)  # определение принадлжености к группам тестовых данных относительно введённой нами модели
    evaluate_model(y_predict, Y_test)  # передача данных для сравнения в следующую функцию

    # pk.dump(model, open('models/saturday', 'wb'))
