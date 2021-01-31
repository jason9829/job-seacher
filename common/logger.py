"""
- Root logger
- Method to change file handler

"""
import logging
import datetime
import os
import sys

ROOT_DIR = os.path.normpath(os.path.join(os.path.abspath(__file__), "..", ".."))
REPO_NAME = os.path.basename(ROOT_DIR)
sys.path.insert(0, ROOT_DIR)

from common.file_manager import FileManager

root_logger = logging.getLogger()
default_format = '%(asctime)s %(levelname)-10s %(filename)-20s %(message)-1s'
message_only_format ='%(message)-1s'


class Logger():
    def __init__(self, filename=REPO_NAME, file_suffix='.log', path=os.path.join(ROOT_DIR, 'log')):
        self.filename = filename + file_suffix
        self.path = os.path.join(path, self.filename)
        FileManager.create_dir_if_not_exist(path)
        logging.basicConfig(
            format=default_format,
            level=logging.INFO,
            #datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[logging.FileHandler(self.path),
                      logging.StreamHandler()])

    def filename_with_timestamp(self, name='log'):
        current_time = datetime.datetime.now()
        return current_time.strftime(name + '_%Y%m%d-%H%M%S.log')
 
    def get_file_handler(self, path, format):
        file_handler = logging.FileHandler(path, 'a')
        formatter = logging.Formatter(format)
        file_handler.setFormatter(formatter)
        return file_handler

    # Ref: https://stackoverflow.com/a/13839732
    def replace_file_handler(self, path, format=message_only_format):
        for hdlr in root_logger.handlers[:]:  # remove all old handlers
            if isinstance(hdlr, logging.FileHandler):
                root_logger.removeHandler(hdlr)
        root_logger.addHandler(self.get_file_handler(path, format))

    def reset_file_handler(self, format=default_format):
        self.replace_file_handler(self.path, format=default_format)


my_logger = Logger()