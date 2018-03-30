import os

def check_path_structure(path, files):

    for f in files:
        if f not in os.listdir(path):
            return False

    return True