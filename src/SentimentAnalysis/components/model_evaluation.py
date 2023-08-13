import os
import pandas as pd
import numpy as np
from SentimentAnalysis.logging import logger
from pathlib import Path
import tensorflow as tf
import joblib
from SentimentAnalysis.entity import ModelEvalutationConfig


class Modevalutation:
    def __init__(self, config: ModelEvalutationConfig):
        self.config = config
        self.threshold = 0.5
    
    def evaluate_and_compare_model(self):
        X_test = np.load(self.config.X_test_data_path)
        y_test = pd.read_csv(self.config.y_test_data_path)

        model = joblib.load(self.config.model_path)
        _, test_accuracy = model.evaluate(X_test, y_test)
        print("Test set accuracy:", test_accuracy)
    
        # Use model.predict to get the probability predictions
        y_test_pred_prob = model.predict(X_test)

        # Convert probability predictions to binary predictions based on the threshold
        y_test_pred_binary = (y_test_pred_prob > self.threshold).astype(int)

        # Flatten the arrays
        y_test_flat = np.ravel(y_test)
        binary_predictions_flat = np.ravel(y_test_pred_binary)

        # Create the actvsPred DataFrame
        actvsPred = pd.DataFrame({'Actual': y_test_flat, 'Predictions': binary_predictions_flat})

        # Print the actvsPred DataFrame
        actvsPred['diff'] = actvsPred['Actual'] - actvsPred['Predictions']
        print(actvsPred.head(20))
        return actvsPred
