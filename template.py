import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

# level is the severity of logging.

project_name =  "TextSummarization"

list_of_files = [
    ".github/workflows/.gitkeep",        # will be used during deployment for CI/CD, empty for now, so that we can upload it right now.
    f"src/{project_name}/__init__.py",   # we need this constructor file, because when we want to import any container as a local package, it will look for this constructor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # It will detect the OS and configure the filepath slashes appropriately
    
    filedir, filename = os.path.split(filepath)
    # as we have a lot of folders that have files inside them, we will use the split function that will return us two things
    
    if filedir != "":
        
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0): # that means that the file is not empty, it has some code so it wont replace it
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    
    else: 
        logging.info(f"{filename} already exists in the directory")
