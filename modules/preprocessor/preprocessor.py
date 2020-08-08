"""
    Задача этого модуля -- предобработка данных
"""
import nltk
import string
from nltk.corpus import stopwords
from pymystem3 import Mystem
from modules.preprocessor.punctuation_and_whitespace import remove_punctuation
from modules.preprocessor.punctuation_and_whitespace import remove_whitespace
import pandas as pd

def remove_garbage(text):

    # removing garbage
    result = ''.join(symbol for symbol in text if not ('a' <= symbol <= 'z' or symbol.isdigit()))
    return result


# removing rows with invalid labels
def remove_bad_labels(data):
    return data[data['labels'].isin(['negative', 'positive', 'neutral'])]


def preprocess_data(data, lemmatiz_isTrue = True):

    # removing invalid rows
    data = remove_bad_labels(data)

    # converting dataframe to list of strs
    text_list = list(data['Text'])

    # Create lemmatizer and stopwords list
    nltk.download("stopwords")
    mystem = Mystem()
    russian_stopwords = stopwords.words("russian")

    # Processing list of str
    for i, v in enumerate(text_list):
        # lower case
        text_list[i] = text_list[i].lower()

        # removing numbers and english
        text_list[i] = remove_garbage(text_list[i])

        # lemmatization
        if lemmatiz_isTrue:
            tokens = mystem.lemmatize(text_list[i])
        else:
            tokens = text_list[i].split()

        # removing stopwords and empty words
        tokens = [token for token in tokens if token not in russian_stopwords and token.strip()]

        # converting list to str
        text_list[i] = " ".join(tokens)

    # removing punctuation and empty spaces
    text_list = remove_punctuation(text_list)
    text_list = remove_whitespace(text_list)

    return text_list


def Test():
    label = ['positive', 'bebe']
    texts =  ['банков 122 !!ds', 'dsek']
    dataf = pd.DataFrame({'Text':texts, 'labels':label})
    print(preprocess_data(dataf))
#Test()