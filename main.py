from predict import predict_data
from train import train_model


if __name__ == "__main__":

    # mode in which programme runs(training a new model or using an existing one)
    # can be set to 'predict' to predict or to 'train' to train
    mode = 'predict'

    # checking 'train' mode
    if mode == 'train':
        train_model('models/sunday')

    # checking 'predict' mode
    elif mode == 'predict':
        predict_data('models/sunday', 'data/comments_klsh.csv', 'output/klsh_predicted.csv')

    # mode error
    else:
        print("Error: unknown mode")
        exit(1)
