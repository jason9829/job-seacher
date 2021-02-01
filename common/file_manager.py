import os


def is_path_exist(path):
    return os.path.exists(path)


def create_dir_if_not_exist(path):
    if not is_path_exist(path):
        os.mkdir(path)