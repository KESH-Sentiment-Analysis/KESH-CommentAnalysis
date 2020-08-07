import string


def remove_punctuation(listofcomments):
    listofclearcomments = []
    for comment in listofcomments:
        translator = str.maketrans('', '', string.punctuation)
        # удаляем знаки препинания
        comment2 = comment.translate(translator)
        listofclearcomments.append(comment2)
    return listofclearcomments


def remove_whitespace(listofcomments):
    listofclearcomments = []
    for comment in listofcomments:
        listofclearcomments.append(" ".join(comment.split()))
    return listofclearcomments
