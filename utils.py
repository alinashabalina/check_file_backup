import logging
import os
import shutil

logger = logging.getLogger(__name__)


class File:
    def __init__(self, current_path, path, name, data):
        self.current_path = current_path
        self.path = path
        self.name = name
        self.data = data
        self.full_path = self.path + f"/{self.name}"
        self.f = open(self.full_path, 'w')

    def __enter__(self):
        if not os.path.isfile(self.full_path):
            shutil.copy(self.current_path + f"/{self.name}", self.path)
            logger.info(f"Copied file {self.name} to {self.path}")
            self.f.write(self.data)
        else:
            print("already there")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print("__exit__")
