import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV


def validator(x_train, y_train, param_grid = {'C': [0.1, 1, 5, 10], 'gamma': [0.5, 5, 10], 'kernel': ['rbf', 'linear']}):
    """пример вызова функции validator():
    C, gamma, kernel = validator(x_train, y_train, your_param_grid)"""

    X_train = x_train[:min(len(x_train),1000) -1]
    Y_train = y_train[:min(len(y_train),1000) -1]

    model = GridSearchCV(SVC(), param_grid)

    # Выбор лучших параметров для data_train
    model.fit(X_train, Y_train)

    # лучшие параметры в формате dict_values([C, gamma, kernel])
    return model.best_params_.values()

