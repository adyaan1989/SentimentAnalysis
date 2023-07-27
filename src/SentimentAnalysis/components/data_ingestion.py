import os
import urllib.request as request
import zipfile
from SentimentAnalysis.logging import logger
from SentimentAnalysis.utils.common import get_size
from pathlib import Path
from SentimentAnalysis.entity import DataIngestionConfig


import urllib.error

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_url,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded with the following info:\n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                logger.error(f"HTTP Error 404: The requested resource was not found at {self.config.source_url}")
            else:
                logger.error(f"HTTP Error {e.code}: {e.reason}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


