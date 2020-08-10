# this module picks the best parameters for the model

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV


def validator(x_train, y_train, param_grid={'kernel': ['rbf', 'linear'], 'C': range(1, 10)}):
    """An example output of the function validator():
    C, kernel = validator(x_train, y_train, your_param_grid)"""

    x_train = x_train[:min(x_train.shape[0], 1000) - 1]
    y_train = y_train[:min(y_train.shape[0], 1000) - 1]

    model = GridSearchCV(SVC(), param_grid)

    # Picking the best parameters
    model.fit(x_train, y_train)

    # returning the best parameters as dict_values([C, kernel])
    return model.best_params_.values()
