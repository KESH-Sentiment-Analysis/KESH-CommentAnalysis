import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import pickle as pk

def vectorizing(docs):

    # инициализируем CountVectorizer()
    cv = pk.load(open('models/count_vectorizer', 'rb'))
    # генерируем ячейки для слов
    word_count_vector = cv.transform(docs)

    # сохраняем векторизатор
    # pk.dump(cv, open('models/count_vectorizer', 'wb'))

    # вычисляем idf
    tfidf_transformer = pk.load(open('models/tfidf_transformer', 'rb'))
    # вычисляем tf-idf
    train_tfidf = tfidf_transformer.transform(word_count_vector)

    #pk.dump(tfidf_transformer, open('models/tfidf_transformer', 'wb'))

    return train_tfidf