import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import pickle as pk

def vectorizing(docs, is_Training):

    # инициализируем CountVectorizer()
    if is_Training == True:
        cv = CountVectorizer(min_df=3, max_df=0.7)
    else:
        cv = pk.load(open('models/count_vectorizer', 'rb'))
    # генерируем ячейки для слов
    if is_Training == True:
        word_count_vector = cv.fit_transform(docs)
    else:
        word_count_vector = cv.transform(docs)

    # сохраняем векторизатор
    # pk.dump(cv, open('models/count_vectorizer', 'wb'))

    # вычисляем idf
    if is_Training == True:
        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
    else:
        tfidf_transformer = pk.load(open('models/tfidf_transformer', 'rb'))
    # вычисляем tf-idf
    if is_Training == True:
        train_tfidf = tfidf_transformer.fit_transform(word_count_vector)
    else:
        train_tfidf = tfidf_transformer.transform(word_count_vector)

    # pk.dump(tfidf_transformer, open('models/tfidf_transformer', 'wb'))

    return train_tfidf