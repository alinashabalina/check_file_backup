import logging
import os
import shutil

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)


class File:
    def __init__(self, current_path, path, name):
        self.f = None
        self.current_path = current_path
        self.path = path
        self.name = name
        self.full_path = self.path + f"/{self.name}"

    def __enter__(self):
        if os.path.isfile(self.full_path) is False:
            shutil.copy(self.current_path + f"/{self.name}", self.path)
            logger.info(f"Copied file {self.name} to {self.path}")
        else:
            logger.info(f"File {self.name} already exists in {self.path}")
        return self

    def open(self, name, method):
        """
        Check open() docs to find more about methods
        'a', 'w', 'x', 'r'
        """
        self.f = open(self.current_path + "/" + name, method)
        logger.info(f"File {self.name} opened and ready to be manipulated with")

    def write(self, data):
        self.f.write(data)
        logger.debug(f"File {self.name} written in")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        logger.info(f"File {self.name} closed successfully")
