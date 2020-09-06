import pip

try:
    import sklearn
except ImportError:
    pip.main(['install', 'sklearn'])

try:
    import numpy
except ImportError:
    pip.main(['install', 'numpy'])

try:
    import pandas
except ImportError:
    pip.main(['install', 'pandas'])

try:
    import matplotlib
except ImportError:
    pip.main(['install', 'matplotlib'])  # this part of code imports needed datasets

from predict import predict_data
from train import train_model
import pandas as pd

if __name__ == "__main__":

    # mode in which programme runs(training a new model or using an existing one)
    # can be set to 'predict' to predict or to 'train' to train
    mode = 'predict'

    # checking 'train' mode
    if mode == 'train':
        train_model('models/sunday')

    # checking 'predict' mode
    elif mode == 'predict':

        n = int(input('Введите количество предложений '))
        data = {'Comment': [input('Введите {0} предложение: '.format(i + 1)) for i in range(n)]}

        df = pd.DataFrame(data, columns=['', 'Comment'])

        predict_data('models/sunday', df, 'output/klsh_predicted.csv')

# mode error
else:
    print("Error: unknown mode")
    exit(1)
