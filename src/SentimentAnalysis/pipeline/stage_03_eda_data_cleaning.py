from SentimentAnalysis.config.configuration import ConfigurationManager
from SentimentAnalysis.components.eda_data_cleaning import DataCleaner
from SentimentAnalysis.logging import logger
from pathlib import Path


STAGE_NAME = "EDA Data Cleaning stage"

class EDADataCleaningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_cleaner_config = config.get_data_clean_config()
        data_cleaner = DataCleaner(config=data_cleaner_config)
        data_cleaner.convert_examples_to_features()
        
if __name__ == "__main__":

    try:

        logger.info(f"--->>-->>>-----> stage {STAGE_NAME} stared <<<<<<<<<<")
        obj = EDADataCleaningPipeline()
        obj.main()
        logger.info(f"....>>>>>>>.....stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e

          




