import os
from SentimentAnalysis.logging import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
from sklearn.preprocessing import LabelBinarizer
import tensorflow as tf
from SentimentAnalysis.entity import EDAdataCleanerConfig

nltk.download('stopwords')
##Setup the English stopwords
stopwords_list = stopwords.words('english')
nltk.download('wordnet')


class DataCleaner:
    def __init__(self, config: EDAdataCleanerConfig):
        self.config = config
        self.tokenizer = ToktokTokenizer()
        self.stopwords_list = set(stopwords.words('english'))
        self.stemmer = SnowballStemmer(language='english')
        self.lb = LabelBinarizer()

    def html(self, text):
        # Remove HTML tags from the text
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()

    def deEmojify(self, text):
        # Remove emojis from the text
        regrex_pattern = re.compile(pattern="["
                                      u"\U0001F600-\U0001F64F"  # emoticons
                                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                      "]+", flags=re.UNICODE)
        return regrex_pattern.sub(r'', text)

    def to_unicode(self, text):
        # Convert text to unicode
        if isinstance(text, float):
            text = str(text)
        if isinstance(text, int):
            text = str(text)
        if not isinstance(text, str):
            text = text.decode('utf-8', 'ignore')
        return text

    def remove_between_square_brackets(self, text):
        # Remove text between square brackets
        return re.sub(r'\[[^]]*\]', '', text)

    def remove_special_characters(self, text, remove_digits=True):
        # Remove special characters and optionally digits
        pattern = r'[^a-zA-z0-9\s]' if remove_digits else r'[^a-zA-z\s]'
        text = re.sub(pattern, '', text)
        return text

    def denoise_text(self, text):
        # Denoise the text using multiple cleaning steps
        text = self.to_unicode(text)
        text = self.html(text)
        text = re.sub(r"http\S+", "", text)
        text = self.deEmojify(text)
        #text = text.encode('ascii', 'ignore')
        #text = text.to_unicode(text)
        text = self.remove_between_square_brackets(text)
        text = self.remove_special_characters(text)
        text = text.lower()
        return text

    def remove_stopwords(self, text, is_lower_case=False):
        # Remove stopwords from the text
        tokens = self.tokenizer.tokenize(text)
        tokens = [token.strip() for token in tokens]
        if is_lower_case:
            filtered_tokens = [token for token in tokens if token not in self.stopwords_list]
        else:
            filtered_tokens = [token for token in tokens if token.lower() not in self.stopwords_list]
        filtered_text = ' '.join(filtered_tokens)
        return filtered_text

    def apply_stemming(self, review):
        # Apply stemming to the text
        return ' '.join([self.stemmer.stem(word) for word in self.tokenizer.tokenize(review)])

    
    def binarize_sentiment(self, sentiment):
        # Binarize sentiment labels (Positive: 1, Negative: 0)
        return self.lb.fit_transform(sentiment)

    def convert_examples_to_features(self):
        data = pd.read_csv(self.config.data_path)
        # Assuming example_batch is a DataFrame with 'review' and 'sentiment' columns
        data['review'] = data['review'].apply(self.denoise_text)
        data['review'] = data['review'].apply(self.remove_stopwords)
        data['review'] = data['review'].apply(self.apply_stemming)
        data['sentiment'] = self.binarize_sentiment(data['sentiment'])

        
        data.to_csv(os.path.join(self.config.root_dir, "data.csv"), index=False)
        logger.info(data.shape)
        print(data.shape)
        logger.info(data.head)
        return data