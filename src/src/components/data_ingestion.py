import sys
import os 
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join('artifacts','data.csv')
    train_data_path = os.path.join('artifacts','train_data.csv')
    test_data_path = os.path.join('artifacts','test_data.csv')
    
    
class DataIngestion:
    
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion Started")
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            
            logging.info("Storing data in a proper format")
            
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False , header=True)
            
            logging.info('train_test_split initiate')
            
            train_data , test_data = train_test_split(df , test_size=0.2 , random_state=42)
            
            
            train_data.to_csv(self.data_ingestion_config.train_data_path, index=False , header=True)
            test_data.to_csv(self.data_ingestion_config.test_data_path, index=False , header=True)
            
            logging.info('Ingestion of Data is done. Train and test data is ready to use')
            
            return(
                
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)   
            
#if __name__=="__main__":
    #obj=DataIngestion()
    #train_data , test_data = obj.initiate_data_ingestion()
    
            
            
            
            
            
            
       