from modules.loader.loader import load_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.fitter.fitter import fit_model
from modules.evaluator.evaluator import evaluate_model
import numpy as np
if __name__ == "__main__":
    print("$ loading data...")
    load_data()

    print("$ preprocessing data...")
    preprocess_data()

    print("$ fitting model...")
    def fit_model (C, kernel, gamma, X_train, Y_train, X_test, Y_test):
        from sklearn import svm
        from sklearn.metrics import recall_score

        model1 = svm.SVC(kernel=kernel, gamma=gamma, C=C)

        model1.fit(X_train, Y_train)
        y_predict = model1.predict(X_test)
        print(recall_score(Y_test, y_predict, average=None))

    print("$ evaluating model...")
    evaluate_model()