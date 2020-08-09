import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV


def validator(x_train, y_train, param_grid={'C': range(1, 10)}):
    """пример вызова функции validator():
    C, gamma, kernel = validator(x_train, y_train, your_param_grid)"""

    X_train = x_train[:min(x_train.shape[0], 1000) - 1]
    Y_train = y_train[:min(y_train.shape[0], 1000) - 1]

    model = GridSearchCV(LinearSVC(), param_grid)

    # Выбор лучших параметров для data_train
    model.fit(X_train, Y_train)

    # лучшие параметры в формате dict_values([C, gamma, kernel])
    return model.best_params_.values()
