# This module trains the model

from sklearn import svm
from modules.fitter.validator import validator
from modules.evaluator.evaluator import evaluate_model


def fit_model(x_train, y_train, x_test, y_test):

    # receiving the parameters
    c, kernel = validator(x_train, y_train)

    # giving the parameters to the model
    model = svm.SVC(kernel=kernel, C=c)

    # training the model on the train data
    model.fit(x_train, y_train)

    # using the model to make predictions about the test data
    y_predict = model.predict(x_test)

    # transferring the prediction results to model evaluating module
    evaluate_model(y_predict, y_test)

    return model
