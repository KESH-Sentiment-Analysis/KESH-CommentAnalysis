# This module evaluates the results of the predictions made by the model

from sklearn.metrics import classification_report


def evaluate_model(y_test, y_pred):
    # naming the classes the results were divided into
    target_names = ['class 0 (positive)', 'class 1 (negative)', 'class 2 (neutral)']

    # outputting the results
    print(classification_report(y_test, y_pred, target_names=target_names))

