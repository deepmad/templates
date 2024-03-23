import os.path


def mkdir(path: str):
    path = path.strip()
    if not os.path.exists(path):
        os.makedirs(path)