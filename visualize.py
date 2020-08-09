import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def histogram_compare(kesh_path, klsh_path):
    # создаём список с названиями солбиков
    cat_par = ['pos', 'neutral', 'neg']
    labels = ['positive', 'neautral', 'negative']

    # два набора данных (КЛШ и КЭШ)
    klsh_data = pd.read_csv(klsh_path)
    klsh_distrib = [3, 2, 1]

    kesh_data = pd.read_csv(kesh_path)
    kesh_distrib = [5, 1, 1]

    # ширина
    width = 0.3
    # создаём столбцы
    x1 = np.arange(1, len(cat_par) + 1)
    x2 = np.arange(1, len(cat_par) + 1)
    # собираем диаграмму по данным
    fig, ax = plt.subplots()
    ax.bar(x1 - width/2, klsh_distrib, width, label='КЛШ')
    ax.bar(x2 + width/2, kesh_distrib, width, label='КЭШ')
    ax.set_xticks(x1)
    # именуем лейблы
    ax.set_xticklabels(cat_par)

    ax.legend()
    # показываем диаграмму
    plt.show()


if __name__ == "__main__":
    histogram_compare('output/kesh_predicted.csv',
                      'output/klsh_predicted.csv')
