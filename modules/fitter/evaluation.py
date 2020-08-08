"""
    Задача этого модуля -- обучение модели
"""
from sklearn.metrics import classification_report


def evaluate_model(y_test, y_pred):
    target_names = ['class 0 (positive)', 'class 1 (negative)', 'class 2 (neutral)']
    print(classification_report(y_test, y_pred, target_names=target_names))


