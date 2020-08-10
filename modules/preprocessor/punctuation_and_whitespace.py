import string


def remove_punctuation(list_of_comments):

    # creating a list for processed comments
    list_of_clear_comments = []

    # processing the comments
    for comment in list_of_comments:
        # initialising a translator
        translator = str.maketrans('', '', string.punctuation)

        # deleting the punctuation using the translator
        comment_clear = comment.translate(translator)

        # adding the processed comment to the list
        list_of_clear_comments.append(comment_clear)

    return list_of_clear_comments


def remove_whitespace(list_of_comments):

    # creating a list for processed comments
    list_of_clear_comments = []

    # processing the comments
    for comment in list_of_comments:
        # removing whitespaces and adding the processed comment to the list
        list_of_clear_comments.append(" ".join(comment.split()))

    return list_of_clear_comments
