import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.commons2 import getsizeb
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download with this information: \n{headers}")
        else:
            logger.info(f"File already exists. Size: {getsizeb(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts zip file into data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

