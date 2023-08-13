import os
import pandas as pd
from SentimentAnalysis.logging import logger
from pathlib import Path
import tensorflow as tf
import joblib
from SentimentAnalysis.entity import ModelTrainerConfig
import numpy as np

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.top_words = 10000
    def train(self):
        X_train = np.load(self.config.X_train_data_path)
        X_test = np.load(self.config.X_test_data_path)

        y_train = pd.read_csv(self.config.y_train_data_path)
        y_test = pd.read_csv(self.config.y_test_data_path)
        

        # Initialize model
        tf.keras.backend.clear_session()

        model = tf.keras.Sequential()
        # Add the embedding layer (Embedding Layer Input = Batch_Size * Length of each review)
        model.add(tf.keras.layers.Embedding(input_dim=self.config.top_words + 1,
                                            output_dim=self.config.embedding_dim,
                                            input_length=self.config.input_length))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.LSTM(units=self.config.rnn_state_size, dropout=self.config.dropout))
        # Use Dense layer for output layer
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Dropout(rate=self.config.dropout))
        model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

        # Compile the model
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Training the model
        history = model.fit(X_train, y_train,
                            epochs=self.config.epochs,
                            batch_size=self.config.batch_size,
                            validation_data=(X_test, y_test))
        
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.saved_model_path))
