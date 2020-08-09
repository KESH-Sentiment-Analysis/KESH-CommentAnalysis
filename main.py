from predict import predict_data
from train import train_model

# import argparse


if __name__ == "__main__":

    # argparse is better
    do_train = True

    if do_train:
        train_model('models/sunday')

    else:
        predict_data('data/comments_kesh_update.csv', 'data/kesh_predicted.csv')
