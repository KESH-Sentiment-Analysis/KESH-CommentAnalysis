"""
    Задача этого модуля -- обучение модели
"""


from sklearn import svm
#from sklearn.metrics import recall_score

def fit_model(X_train, Y_train, X_test, Y_test):
    C, gamma, kernel = validator(examp.take(np.random.permutation(len(data_train))[:min(len(data_train),1000)-1]) #получение необходимых параметров
    model = svm.SVC(kernel=kernel, gamma=gamma, C=C) #модель принимает необходимые параметры
    model.fit(X_train, Y_train) #модель обучается на тренировочных данных
    evaluate_model(X_test, Y_test)

