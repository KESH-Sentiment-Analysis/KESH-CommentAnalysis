"""
    Задача этого модуля -- обучение модели
"""
from sklearn.metrics import classification_report


def evaluation_model(model, test_data):
    """Здесь будет ваша модель"""
    target_names = ['class 0 (positive)', 'class 1 (negative)', 'class 2 (neutral)']
    y_pred = model.predict(test_data['Text'].toarray)
    print(classification_report(test_data['Labels'], y_pred, target_names=target_names))


# 0 - positive
# 1 - negative
# 2 - neutral
#mas = [('Ужасный товар!', 1), ('Рекомендую. Все супер!', 0), ('Здесь продают столы', 2)]
#evaluation_model(mas, y_pred)
