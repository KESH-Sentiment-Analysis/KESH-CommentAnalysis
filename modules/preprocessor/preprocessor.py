"""
    Задача этого модуля -- предобработка данных
"""
import nltk
import string
from nltk.corpus import stopwords
from pymystem3 import Mystem


def remove_garbage(text):

    # removing garbage
    result = ''.join(symbol for symbol in text if not ('a' <= symbol <= 'z' or symbol.isdigit()))
    return result


def preprocess_data(text, lemmatiz_isTrue = True, tokenization_isTrue = True):
    nltk.download("stopwords")
    # Create lemmatizer and stopwords list
    mystem = Mystem()
    russian_stopwords = stopwords.words("russian")
    
    # lower case
    text = text.lower()
    
    # removing numbers and english
    text = remove_garbage(text)
    
    # lemmatization
    if lemmatiz_isTrue:
        tokens = mystem.lemmatize(text)
    else:
        tokens = text.split()

    # removing punctuation and empty words   
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    tokens = [token for token in stripped if token not in russian_stopwords and token.strip()]
    
    # tokeniztion
    if tokenization_isTrue:
        return tokens
    else:
        text = " ".join(tokens)
        return text


def Test():
    print(preprocess_data("мне понравилась английская булочка с чаем!!??,,dffisj"))
#Test()