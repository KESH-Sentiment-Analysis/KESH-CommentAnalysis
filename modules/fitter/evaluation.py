"""
    Задача этого модуля -- обучение модели
"""
from sklearn.metrics import classification_report
import pandas as pd


def evaluation_model(model, test):
    """Здесь будет ваша модель"""
    for i in test:
        y_pred.append(fit_model(i))
    y_true = []
    model.drop(columns=0, inplace=True)
    y_pred = model.array
    target_names = ['class 0 (positive)', 'class 1 (negative)', 'class 2 (neutral)']
    print(classification_report(y_true, y_pred, target_names=target_names))


# 0 - positive
# 1 - negative
# 2 - neutral
#mas = [('Ужасный товар!', 1), ('Рекомендую. Все супер!', 0), ('Здесь продают столы', 2)]
#evaluation_model(mas, y_pred)
