import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV



def validator(data_train, param_grid = {'C': [0.1, 1, 5, 10], 'gamma': [0.5, 5, 10], 'kernel': ['rbf', 'linear']}):
    """пример вызова функции validator()
    C, gamma, kernel = validator(example, your_param_grid)"""

    data_train = data_train[:min(len(data_train),1000) -1]

    model = GridSearchCV(SVC(), param_grid)

    # Разделение данных на фичи и цели
    Y_train = data_train['labels']
    X_train = data_train.drop('labels', axis=1)

    # Выбор лучших параметров для data_train
    model.fit(X_train, Y_train)

    # лучшие параметры в формате dict_values([C, gamma, kernel])
    return model.best_params_.values()