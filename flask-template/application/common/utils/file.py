import os.path


def mkdir(path: str):
    path = path.strip()
    if not os.path.exists(path):
        os.makedirs(path)


def subfix(filename: str) -> str:
    if filename.rfind('.') == -1:
        return ''
    return filename[filename.rfind('.')+1:]
