# this module visualises the predicted data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def count_labels(data):
    # converting data into lists depending on the label
    data_pos = data[data['Label'] == 'positive']['Comment'].to_list()
    pos = len(data_pos)
    data_neu = data[data['Label'] == 'neautral']['Comment'].to_list()
    neu = len(data_neu)
    data_neg = data[data['Label'] == 'negative']['Comment'].to_list()
    neg = len(data_neg)

    # making a list out of number of comments with different labels
    result = [pos, neu, neg]
    return result


def histogram_compare(file):
    # creating a list with bar names
    cat_par = ['positive', 'neutral', 'negative']

    df = pd.read_csv(file, delimiter=',')

    # creating a list out of data distribution
    data_distrib = count_labels(df)

    # setting the width
    width = 0.6

    # creating the bars
    x1 = np.arange(1, len(cat_par) + 1)

    # compiling the diagram
    fig, ax = plt.subplots()
    ax.bar(x1 - width/2, data_distrib, width, label='Data')
    ax.set_xticks(x1)

    # naming the labels
    ax.set_xticklabels(cat_par)

    ax.legend()
    # showcasing the diagram
    plt.show()


def test():
    file_path = '../../*.csv'
    histogram_compare(file_path)
#test()
