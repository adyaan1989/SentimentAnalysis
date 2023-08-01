from SentimentAnalysis.logging import logger

from SentimentAnalysis.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline
from SentimentAnalysis.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

# from TextSummarizer.pipeline.stage_03_data_transfromation import DataTransformationTrainingPipeline
# from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
# from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"--->>-->>>-----> stage {STAGE_NAME} stared <<<<<<<<<<")
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"....>>>>>>>.....stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# STAGE_NAME = "Data Validation Stage"

# try:
#     logger.info(f"--->>-->>>-----> stage {STAGE_NAME} stared <<<<<<<<<<")
#     data_validation = DataValidationTrainingPipeline()
#     data_validation.main()
#     logger.info(f"....>>>>>>>.....stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e
