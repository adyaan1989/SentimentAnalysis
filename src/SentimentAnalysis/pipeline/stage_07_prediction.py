from SentimentAnalysis.config.configuration import ConfigurationManager
from SentimentAnalysis.components.eda_data_cleaning import DataCleaner
import tensorflow as tf
import joblib
from SentimentAnalysis.logging import logger


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_prediction_config()
        self.data_cleaner = DataCleaner(self.config)
        self.max_review_length = 300
        #self.tokenizer = tf.keras.preprocessing.text.Tokenizer()
        self.model = joblib.load(self.config.final_model_path)
        self.token = joblib.load('dataStore/data_transformation/tokenizer.joblib')
        
    def predict(self, text):
        #user_input = input("Enter a review: ")
        # Clean the user input using DataCleaner methods
        text = self.data_cleaner.denoise_text(text)  # Call denoise_text on the instance
        text = self.data_cleaner.remove_stopwords(text)  # Call remove_stopwords on the instance
        text = self.data_cleaner.apply_stemming(text)  # Call apply_stemming on the instance
        print("Cleaned input:", text)

        # Tokenize and pad the input
        user_input_sequence = self.token.texts_to_sequences([text])
        print("User input sequence:", user_input_sequence)

        user_input_padded = tf.keras.preprocessing.sequence.pad_sequences(user_input_sequence, self.max_review_length, padding='pre')
        print("User input padded:", user_input_padded)

        # Make prediction
        prediction_prob = self.model.predict(user_input_padded)[0][0]
        
        # Display the result
        if prediction_prob > 0.5:
            predicted_sentiment = "Positive"
        
        else:
            predicted_sentiment = "Negative"

        # Print the predicted sentiment along with the message
        print("Predicted Sentiment:", predicted_sentiment)
        print("Probability:", prediction_prob)

        return predicted_sentiment