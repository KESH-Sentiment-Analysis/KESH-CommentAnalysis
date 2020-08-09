from modules.loader.loader import give_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.preprocessor.vectorization import vectorizing
from modules.preprocessor.separate_data import data_separator
from modules.fitter.fitter import fit_model
import pickle as pk
import pandas as pd

if __name__ == "__main__":

    is_Training = True

    print("$ loading data...")
    data_frame = give_data('data/corpus_sent.csv', is_Training)

    print("$ preprocessing data...")
    if is_Training == True:
        str_list, new_labels = preprocess_data(data_frame, is_Training)
    else:
        str_list = preprocess_data(data_frame, is_Training)

    #print(str_list)

    matrix = vectorizing(str_list, is_Training)
    if is_Training == True:
        x_train, x_test, y_train, y_test = data_separator(matrix, new_labels.array, 20)

    if is_Training:
        print("$ fitting model...")
        fit_model(x_train, y_train, x_test, y_test)
    else:
        model = pk.load(open('models/saturday', 'rb'))
        predicted_list = model.predict(matrix)
        data = {'Comment': str_list, 'Label': predicted_list}
        predicted = pd.DataFrame(data=data)
        #predicted.to_csv('data/comments_kesh_predicted.csv')
        print(predicted)
