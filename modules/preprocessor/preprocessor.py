"""
    Задача этого модуля -- предобработка данных
"""
# import nltk
# import string
# from nltk.corpus import stopwords
# from pymystem3 import Mystem
from modules.preprocessor.punctuation_and_whitespace import remove_punctuation
from modules.preprocessor.punctuation_and_whitespace import remove_whitespace
import pandas as pd
import numpy as np


def remove_garbage(text):

    # removing garbage
    result = ''.join(symbol for symbol in text if not ('a' <= symbol <= 'z' or symbol.isdigit()))
    return result


def remove_bad_labels(data):
    # removing rows with invalid labels
    return data[data['Labels'].isin(['negative', 'positive', 'neautral'])]


def preprocess_data(data, text_col_name, has_labels=True):

    if has_labels:
        print("# removing rows with invalid labels")
        data = remove_bad_labels(data)

    data = data.astype(str)
    data = data[(data[text_col_name] != np.nan) | (data[text_col_name] != '')]

    print("# converting dataframe to list of strs")
    text_list = data[text_col_name].to_list()

    # print("# Create lemmatizer and stopwords list")
    # nltk.download("stopwords")
    # mystem = Mystem()
    # russian_stopwords = stopwords.words("russian")

    print("# Processing list of str")
    for i, v in enumerate(text_list):

        # lower case
        text_list[i] = text_list[i].lower()

        # removing numbers and english
        text_list[i] = remove_garbage(text_list[i])

        # lemmatization
        # if lemmatiz_isTrue:
        #     # tokens = mystem.lemmatize(text_list[i])
        # else:
        # tokens = text_list[i].split()
        #
        # # converting list to str
        # text_list[i] = " ".join(tokens)

    print("# removing punctuation and empty spaces")
    text_list = remove_punctuation(text_list)
    text_list = remove_whitespace(text_list)

    data = data.drop([text_col_name], axis=1)
    data[text_col_name] = text_list

    data = data[data[text_col_name] != '']

    return data


def test():
    label = ['positive', 'bebe']
    texts = ['банков 122 !!ds', 'dsek']
    df = pd.DataFrame({'Text': texts, 'labels': label})
    print(preprocess_data(df))
