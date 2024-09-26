import os
import sys
from pathlib import Path

project_name = 'Kindle-Review'

list_of_files = [
    
    f"{project_name}/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_train.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/data_pusher.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/commons.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/configuration_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
    "template/home.html",
    "template/index.html",
    
]

for filepath in list_of_files:
    filepath  = Path(filepath)
    filedir , filename  = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath , 'w') as f:
            pass
    else:
        print(f"file is already presented as: {filepath} already exists")
        
        