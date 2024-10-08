import sys
import os 
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from src.Kindle-Review.exception import CustomException
from src.Kindle-Review.logger import logging
from dataclasses import dataclass
from src.Kaggle-Review.component.data_ingestion  import DataIngestionConfig
from src.Kaggle-Review.component.data_ingestion  import DataIngestion



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def start_data_ingestion(self):
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e, sys)
        
    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()

        except Exception as e:
            raise CustomException(e, sys) 