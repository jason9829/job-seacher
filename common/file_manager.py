import os

class FileManager():
    @classmethod
    def is_path_exist(self, path):
        return os.path.exists(path)

    @classmethod
    def create_dir_if_not_exist(self, path):
        if not self.is_path_exist(path):
            os.mkdir(path)