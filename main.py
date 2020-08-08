from modules.loader.loader import give_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.preprocessor.vectorization import vectorizing
from modules.preprocessor.separate_data import data_separator
from modules.fitter.fitter import fit_model

if __name__ == "__main__":
    print("$ loading data...")
    data_frame = give_data('data/corpus_sent.csv')

    print("$ preprocessing data...")
    str_list, new_labels = preprocess_data(data_frame)

    print(str_list)

    matrix = vectorizing(str_list)
    x_train, x_test, y_train, y_test = data_separator(matrix, new_labels.array, 25)

    print("$ fitting model...")
    fit_model(x_train, y_train, x_test, y_test)
