# This module loads the data

import pandas as pd


def give_data(file_name, do_shuffle=True):

    # reading file with examples
    df = pd.read_csv(file_name, delimiter=',')

    # removing the numeration row
    df = df.drop(['Unnamed: 0'], axis=1)

    # shuffling dataframe
    if do_shuffle:
        df = df.sample(frac=1).reset_index(drop=True)

    return df


def test():
    # loading the input file
    file = "../../data/corpus_sent.csv"
    print(give_data(file))
# test()
