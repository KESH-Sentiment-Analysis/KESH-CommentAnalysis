import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import pickle as pk

def vectorizing(docs):

    # инициализируем CountVectorizer()
    cv = CountVectorizer(min_df=3, max_df=0.7)
    # генерируем ячейки для слов
    word_count_vector = cv.fit_transform(docs)

    # сохраняем векторизатор
    pk.dump(cv, open('models/count_vectorizer', 'wb'))

    # вычисляем idf
    tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
    # вычисляем tf-idf
    train_tfidf = tfidf_transformer.fit_transform(word_count_vector)

    pk.dump(tfidf_transformer, open('models/tfidf_transformer', 'wb'))

    return train_tfidf