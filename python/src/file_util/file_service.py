import os
from typing import List


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

    def list_files(self, path_to_dir) -> List[str]:
        return os.listdir(path_to_dir)

    def get_count_of_files(self, path_to_dir) -> int:
        return len(self.list_files(path_to_dir))
