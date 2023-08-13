
from SentimentAnalysis.constants import *
from SentimentAnalysis.utils.common import read_yaml
from SentimentAnalysis.utils.common import create_directories
from SentimentAnalysis.entity import (DataIngestionConfig,
                                      DataValidationConfig,
                                      EDAdataCleanerConfig,
                                      DataTransformationConfig,
                                      ModelTrainerConfig,
                                      ModelEvalutationConfig,
                                      ModelPredictionConfig)



class ConfigurationManager:
    
    def __init__(
                self,
                config_file_path = CONFIG_FILE_PATH,
                params_file_path = PARAMS_FILE_PATH,
                schema_filepath = SCHEMA_FILE_PATH):
            

            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_file_path)
            self.schema = read_yaml(schema_filepath)

            create_directories([self.config.dataStore_root])

    #Data Inegetion 
    def get_data_ingestion_config(self)-> DataIngestionConfig:
          config = self.config.data_ingestion

          create_directories([config.root_dir])
          

          data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_url=config.source_url,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir

          )     
          return data_ingestion_config 


    #Data Validation  
    def get_data_validation_config(self)-> DataValidationConfig:
          config = self.config.data_validation
          schema = self.schema.COLUMNS

          create_directories([config.root_dir])
         
          data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                unzip_data_dir=config.unzip_data_dir,
                all_schema=schema,
          )     
          return data_validation_config
     

    # EDA and data cleaning function
    def get_data_clean_config(self)-> EDAdataCleanerConfig:
          config = self.config.EDA_DataCleaner

          create_directories([config.root_dir])
          
          data_cleaner_config = EDAdataCleanerConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
               
          )     
          return data_cleaner_config   
      
    #Data Transformatins
    def get_data_transformation_config(self)-> DataTransformationConfig:
          config = self.config.data_transformation

          create_directories([config.root_dir])
          
          data_transformation_config = DataTransformationConfig(
                root_dir=config.root_dir,
                clean_data_path=config.clean_data_path,
                tokenizer_path=config.tokenizer_path
   
          )     
          return data_transformation_config
    
    #Model Trainer
    def get_model_trainer_config(self) -> ModelTrainerConfig:
            config = self.config.model_trainer
            params = self.params.model_parameters
            model_trainer = self.params.model_training_parameters

            #schema = self.schema.TARGET_COLUMN

            create_directories([config.root_dir])

            model_trainer_config = ModelTrainerConfig(
                  root_dir = config.root_dir,
                  X_train_data_path = config.X_train_data_path,
                  y_train_data_path=config.y_train_data_path,
                  X_test_data_path = config.X_test_data_path,
                  y_test_data_path=config.y_test_data_path,
                  saved_model_path = config.saved_model_path,
                  top_words = params.top_words,
                  input_length = params.input_length,
                  embedding_dim = params.embedding_dim,
                  rnn_state_size = params.rnn_state_size,
                  dropout = params.dropout,
                  epochs=model_trainer.epochs,
                  batch_size=model_trainer.batch_size,
                  #target_column=schema.name
            )     
            return model_trainer_config
    
    #Model Evaluation
    def get_model_evaluation_config(self) -> ModelEvalutationConfig:
          config = self.config.model_evaluation

          create_directories([config.root_dir])

          model_evaluation_config = ModelEvalutationConfig(
                root_dir=config.root_dir,
                X_test_data_path=config.X_test_data_path,
                y_test_data_path=config.y_test_data_path,
                model_path=config.model_path,
                #metric_file_name=config.metric_file_name

          )

          return model_evaluation_config
    

    # Prediction
    def get_model_prediction_config(self) -> ModelPredictionConfig:
          config = self.config.model_prediction

          create_directories([config.root_dir])

          model_prediction_config = ModelPredictionConfig(
                root_dir=config.root_dir,
                final_model_path=config.final_model_path,
                save_model_performance=config.save_model_performance,

      )

          return model_prediction_config
    


