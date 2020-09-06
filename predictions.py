from modules.loader.loader import give_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.preprocessor.vectorization import vectorizing
from modules.preprocessor.separate_data import data_separator
from modules.fitter.fitter import fit_model
import pickle
import pandas as pd

test_data = pd.read_csv('data/cleared_data (1).csv')
model = pickle.load(open("models/saturday", 'rb'))
CV = pickle.load(open('models/count_vectorizer', 'rb'))
trans = CV.transform(test_data['Comment'].to_list())
tfidf = pickle.load(open('models/tfidf_transformer', 'rb'))
train_tfidf = tfidf.transform(trans)

predictions = model.predict(train_tfidf)

results = pd.DataFrame({'results': predictions})

results.to_csv("predictions.csv")

test_data["sentiment"] = predictions

test_data.to_csv("whole_test_data.csv")

