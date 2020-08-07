"""
    Задача этого модуля -- обучение модели
"""

# импортируй здесь нужные тебе библиотеки
# from ... import ...
from sklearn import svm
from sklearn.metrics import recall_score

def fit_model(C, kernel, gamma, X_train, Y_train, X_test, Y_test):
    model = svm.SVC(kernel=kernel, gamma=gamma, C=C) #модель получает необходимые параметры
    model.fit(X_train, Y_train) #модель обучается на тренировочных данных
    y_predict = model1.predict(X_test) #модель определяет принадлежность к группам у тестовых данных
    print(recall_score(Y_test, y_predict, average=None)) #приблезительная оценка точности определения модели

