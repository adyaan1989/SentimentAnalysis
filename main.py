from SentimentAnalysis.logging import logger

from SentimentAnalysis.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline
from SentimentAnalysis.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from SentimentAnalysis.pipeline.stage_03_eda_data_cleaning import EDADataCleaningPipeline
from SentimentAnalysis.pipeline.stage_04_data_transformation import DataTransformationPipeline
from SentimentAnalysis.pipeline.stage_05_model_trainer import ModelTrainingPipeline
from SentimentAnalysis.pipeline.stage_06_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"--->>-->>>-----> stage {STAGE_NAME} stared <<<<<<<<<<")
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"....>>>>>>>.....stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"--->>-->>>-----> stage {STAGE_NAME} stared <<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"....>>>>>>>.....stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "EDA Data Cleaning Stage"

try:
    logger.info(f"--->>-->>>-----> stage {STAGE_NAME} stared <<<<<<<<<<")
    data_cleaner = EDADataCleaningPipeline()
    data_cleaner.main()
    logger.info(f"....>>>>>>>.....stage {STAGE_NAME} completed <<<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:

    logger.exception(e)
    raise e

STAGE_NAME = "ModelTraining"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e            

STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e            

