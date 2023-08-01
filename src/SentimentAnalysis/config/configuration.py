
from SentimentAnalysis.constants import *
from SentimentAnalysis.utils.common import read_yaml
from SentimentAnalysis.utils.common import create_directories
from SentimentAnalysis.entity import (DataIngestionConfig,
                                      DataValidationConfig)



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

          create_directories([config.root_dir])
          

          data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
                
          )     
          return data_validation_config

