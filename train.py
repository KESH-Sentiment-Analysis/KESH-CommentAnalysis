from modules.loader.loader import give_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.preprocessor.vectorization import vectorizing
from modules.preprocessor.separate_data import data_separator
from modules.fitter.fitter import fit_model

import pickle as pk


def train_model(model_output_path):

    print("$ loading data...")
    data_frame = give_data('data/corpus_sent.csv')

    print("$ preprocessing data...")
    data_frame = preprocess_data(data_frame, 'Text')

    print("$ vectorizing texts...")
    matrix = vectorizing(data_frame['Text'].to_list(), False)
    x_train, x_test, y_train, y_test = data_separator(matrix, data_frame['Labels'].array, 20)

    print("$ fitting model...")
    model = fit_model(x_train, y_train, x_test, y_test)

    print("$ dumping model...")
    pk.dump(model, open(model_output_path, 'wb'))
