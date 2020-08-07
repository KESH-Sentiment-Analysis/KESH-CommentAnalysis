from modules.loader.loader import load_data
from modules.preprocessor.preprocessor import preprocess_data
from modules.fitter.fitter import fit_model
from modules.evaluator.evaluator import evaluate_model
import numpy as np
if __name__ == "__main__":
    print("$ loading data...")
    load_data()

    print("$ preprocessing data...")
    preprocess_data()

    print("$ fitting model...")
    fit_model()

    print("$ evaluating model...")
    evaluate_model()