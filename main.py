from predict import predict_data
from train import train_model

# import argparse


if __name__ == "__main__":

    mode = 'predict'
    # mode = 'predict'
    # argparse is better for this

    if mode == 'train':
        train_model('models/sunday')

    elif mode == 'predict':
        predict_data('models/sunday', 'data/comments_klsh.csv', 'output/klsh_predicted.csv')

    else:
        print("Error: unknown mode")
        exit(1)
