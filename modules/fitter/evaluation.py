"""
    Задача этого модуля -- обучение модели
"""
from sklearn.metrics import classification_report


def evaluate_model(model, test_x, test_y):
    target_names = ['class 0 (positive)', 'class 1 (negative)', 'class 2 (neutral)']
    y_pred = model.predict(test_x)
    print(classification_report(test_y, y_pred, target_names=target_names))
