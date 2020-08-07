import string


def remove_punctuation(list_of_comments):
    # создаем список, где будут лежать обработанные комментарии
    list_of_clear_comments = []
    # пробегаемся по всем комментариям в сыром списке
    for comment in list_of_comments:
        translator = str.maketrans('', '', string.punctuation)
        # удаляем знаки препинания с помощью созданной функции трансляторя
        comment2 = comment.translate(translator)
        # добавляем обработанный комментарий в список
        list_of_clear_comments.append(comment2)
    return list_of_clear_comments


def remove_whitespace(list_of_comments):
    # создаем список, где будут лежать обработанные комментарии
    list_of_clear_comments = []
    # пробегаемся по всем комментариям в сыром списке
    for comment in list_of_comments:
        # обрабатываем и добавляем обработанный комментарий в список
        list_of_clear_comments.append(" ".join(comment.split()))
    return list_of_clear_comments
