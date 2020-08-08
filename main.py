from modules.loader.loader import give_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.preprocessor.vectorization import vectorizing
from modules.preprocessor.separate_data import data_separator

if __name__ == "__main__":
    print("$ loading data...")
    data_frame = give_data('corpus_sent.csv')

    print("$ preprocessing data...")
    str_list = preprocess_data(data_frame)
    matrix = vectorizing(str_list)
    sep_vectors = data_separator(matrix)


    print("$ fitting model...")
    fit_model()

    print("$ evaluating model...")
    evaluate_model()