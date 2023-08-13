from SentimentAnalysis.config.configuration import ConfigurationManager
from SentimentAnalysis.components.model_evaluation import Modevalutation
from SentimentAnalysis.logging import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        model_evaluation_config = config_manager.get_model_evaluation_config()
        model_evaluation_config = Modevalutation(config=model_evaluation_config)
        model_evaluation_config.evaluate_and_compare_model()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
    raise e            

