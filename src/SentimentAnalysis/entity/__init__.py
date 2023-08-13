from dataclasses import dataclass
from pathlib import Path


#Data Ingestion Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


#Data Validation Path   
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: list
    all_schema: dict


#EDA file and data cleaning config
@dataclass(frozen=True)
class EDAdataCleanerConfig:
    root_dir: Path
    data_path: Path
    

#data tranformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    clean_data_path: Path
    tokenizer_path: str


# Model Trainer
@dataclass(frozen=True)
class ModelTrainerConfig: 
    root_dir: Path
    X_train_data_path: Path
    y_train_data_path: Path
    X_test_data_path: Path
    y_test_data_path: Path
    saved_model_path: str
    top_words: int
    input_length: int
    embedding_dim: int
    rnn_state_size: int
    dropout: float
    epochs: int
    batch_size: int
    
#Model Evaluation
@dataclass(frozen=True)
class ModelEvalutationConfig: 
    root_dir: Path
    X_test_data_path: Path
    y_test_data_path: Path
    model_path: Path

#Model Predictions
@dataclass(frozen=True)
class ModelPredictionConfig: 
    root_dir: Path
    final_model_path: Path
    save_model_performance: str 