import os
from SentimentAnalysis.logging import logger
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
from SentimentAnalysis.entity import DataTransformationConfig
import tensorflow as tf
import numpy as np
import joblib


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.top_words = 10000
        self.tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
        self.max_review_length = 300

    def preprocess_and_pad_sequences(self):
        df = pd.read_csv(self.config.clean_data_path)
        
        ##Split the data into training and test sets ratio 80% and 20%
        train, test, y_train, y_test = train_test_split(df['review'],
                                                        df['sentiment'],
                                                        test_size=0.2,
                                                        random_state=42)
        
        #np.save(os.path.join(self.config.root_dir, "train.npy"), train)
        
        print("train data shape", train.shape, "test data shape", test.shape)
        logger.info(train.head())

        # Building the Tokenizer
        self.tokenizer.fit_on_texts(train.tolist())
        joblib.dump(self.tokenizer, os.path.join(self.config.root_dir, self.config.tokenizer_path))
           

        print("#"*100)

        logger.info(print("token",self.tokenizer.word_index))

        X_train = self.tokenizer.texts_to_sequences(train.tolist())
        X_test = self.tokenizer.texts_to_sequences(test.tolist())

        def find_longest_sequence_length(X):
            # Use list comprehension to calculate the lengths of all sequences
            sequence_lengths = [len(sequence) for sequence in X]

            # Find the maximum length among all the sequences
            max_length = max(sequence_lengths)

            return max_length

        # Call the function to find maximum sequence lengths for train and test data
        max_length_X_train = find_longest_sequence_length(X_train)
        max_length_X_test = find_longest_sequence_length(X_test)

        # Print the result
        logger.info(print("Maximum sequence length for X_train:", max_length_X_train))
        logger.info(print("Maximum sequence length for X_test:", max_length_X_test))

        # Pre Pad training and test reviews
        X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, self.max_review_length, padding='pre')
        X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, self.max_review_length, padding='pre')
        
        # Save preprocessed data as CSV files (optional, you can adjust this based on your requirements)
        np.save(os.path.join(self.config.root_dir, "X_train.npy"), X_train)
        y_train.to_csv(os.path.join(self.config.root_dir, "y_train"), index=False)
        
        np.save(os.path.join(self.config.root_dir, "X_text.npy"), X_test)
        y_test.to_csv(os.path.join(self.config.root_dir, "y_test"), index=False)

        print("transformed data")
        logger.info(X_train[0:1])
               