from modules.loader.loader import give_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.preprocessor.vectorization import vectorizing
from visualize import histogram_compare
import pickle as pk
import pandas as pd


def predict_data(model_path, data_path, output_path):

    print("$ loading data...")
    data_frame = give_data(data_path, False)

    print("$ preprocessing data...")
    data_frame = preprocess_data(data_frame, 'Comment', False)

    print("$ vectorizing data...")
    matrix = vectorizing(data_frame['Comment'], False)

    print("$ loading model...")
    model = pk.load(open(model_path, 'rb'))

    print("$ predicting...")
    predicted_list = model.predict(matrix)
    data = {'Comment': data_frame['Comment'].to_list(), 'Label': predicted_list}
    predicted = pd.DataFrame(data=data)

    print("$ writing to file...")
    predicted.to_csv(output_path)
    
    histogram_compare(output_path)

    print(predicted)
