from SentimentAnalysis.config.configuration import ConfigurationManager
from SentimentAnalysis.components.data_validation import DataValidation
from SentimentAnalysis.logging import logger

STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        
    
if __name__ == "__main__":
    try:
        logger.info(f"--->>-->>>-----> stage {STAGE_NAME} stared <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"....>>>>>>>.....stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


