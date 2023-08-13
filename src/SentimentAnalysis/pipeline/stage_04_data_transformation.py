from SentimentAnalysis.config.configuration import ConfigurationManager
from SentimentAnalysis.components.data_transformation import DataTransformation
from SentimentAnalysis.logging import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
            try:
                  
                with open(Path("dataStore/data_validation/status.txt"), "r") as f:
                        status = f.read().split(" ")[-1]
                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation_config)
                    data_transformation.preprocess_and_pad_sequences()
            
                else:
                     raise Exception("Data Schema is not valid")

            
            except Exception as e:
                print(e)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
    raise e            
