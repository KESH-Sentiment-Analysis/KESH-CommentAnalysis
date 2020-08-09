"""
    Задача этого модуля -- обучение модели
"""

from sklearn import svm
from modules.fitter.validator import validator
from modules.evaluator.evaluator import evaluate_model


def fit_model(x_train, y_train, x_test, y_test):
    # получение необходимых параметров
    c, kernel = validator(x_train, y_train)

    # модель принимает необходимые параметры
    model = svm.SVC(kernel=kernel, C=c)

    # модель обучается на тренировочных данных
    model.fit(x_train, y_train)

    # определение принадлжености к группам тестовых данных относительно введённой нами модели
    y_predict = model.predict(x_test)
    # передача данных для сравнения в следующую функцию
    evaluate_model(y_predict, y_test)

    return model
