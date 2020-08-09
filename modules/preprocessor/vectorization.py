from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import pickle as pk


def vectorizing(docs, is_training):

    if is_training:
        # инициализируем CountVectorizer()
        cv = CountVectorizer(min_df=3, max_df=0.7)

        # векторизуем тексты
        word_count_vector = cv.fit_transform(docs)
        pk.dump(cv, open('models/count_vectorizer', 'wb'))

        # инициализируем tf-idf
        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)

        # трансформируем тексты с tf-idf
        train_tfidf = tfidf_transformer.fit_transform(word_count_vector)
        pk.dump(tfidf_transformer, open('models/tfidf_transformer', 'wb'))

    else:
        # векторизуем тексты
        cv = pk.load(open('models/count_vectorizer', 'rb'))
        word_count_vector = cv.transform(docs)

        # трансформируем тексты с tf-idf
        tfidf_transformer = pk.load(open('models/tfidf_transformer', 'rb'))
        train_tfidf = tfidf_transformer.transform(word_count_vector)

    return train_tfidf
