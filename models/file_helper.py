import os


class FileHelper:
    def __init__(self):
        pass

    @staticmethod
    def file_exists(filename: str) -> bool:
        return os.path.isfile(os.path.expanduser(filename))

    @staticmethod
    def path_exists(path: str) -> bool:
        return os.path.isdir(os.path.expanduser(path))

    @staticmethod
    def get_expanded_filename(filename: str) -> str:
        if FileHelper.file_exists(filename=filename):
            return os.path.expanduser(filename)
        else:
            raise FileNotFoundError(f'Bestand "{filename}" bestaat niet.')

    @staticmethod
    def get_expanded_path(path: str) -> str:
        if FileHelper.path_exists(path=path):
            return os.path.expanduser(path)
        else:
            raise NotADirectoryError(f'Directory "{path}" bestaat niet.')