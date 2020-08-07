"""
    Задача этого модуля -- предобработка данных
"""

# импортируй здесь нужные тебе библиотеки
# from ... import ...
import re
import nltk
import string
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result
def remove_english(text):
    results = list(text)
    copyres = results.copy()
    for result in results:
        if result >= 'a' and result <= 'z':
            copyres.remove(result)
    return copyres
def preprocess_data(text, lemmatiz_isTrue = True, tokenization_isTrue = True):
    nltk.download("stopwords")
    # Create lemmatizer and stopwords list
    mystem = Mystem()
    russian_stopwords = stopwords.words("russian")
    text = text.lower()
    text = remove_numbers(text)
    text = remove_english(text)
    strtext = ''.join([str(elem) for elem in text])
    if lemmatiz_isTrue:
        tokens = mystem.lemmatize(strtext)
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    tokens = [token for token in stripped if token not in russian_stopwords and token != " " and len(token.strip())]
    if tokenization_isTrue:
        return tokens
    else:
        strtext = " ".join(tokens)
        return strtext
print(preprocess_data('мне    понравилась та французская булочка с чаем fjifs2223?!'))