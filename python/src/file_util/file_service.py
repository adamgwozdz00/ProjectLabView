import os


class FileService:

    def create_dir_if_not_exists(self, path_to_dir: str) -> None:
        if self.is_exists(path_to_dir):
            return

        os.mkdir(path_to_dir)

    def clean_dir(self, path_to_dir):
        for file in os.listdir(path_to_dir):
            os.remove(f'{path_to_dir}/{file}')

    def is_exists(self, path: str) -> bool:
        if os.path.isdir(path):
            return True
        if os.path.isfile(path):
            return True
        return False
