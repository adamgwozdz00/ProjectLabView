import pathlib


class Configuration:

    _PATH = pathlib.Path(__file__).parent.resolve()

    def get_annotations_path(self) -> str:
        pass

    def get_image_path(self) -> str:
        pass

    def get_dirs_path(self) -> str:
        pass
