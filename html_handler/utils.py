import os

def create_dir_if_not_exists(path: str):
    if not os.path.isdir(path):
        print("WARNING {path} doesn't exists, creating one...")
        os.mkdir(path)

