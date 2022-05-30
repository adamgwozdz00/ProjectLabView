from src.application.configuration import Configuration


class StaticConfiguration(Configuration):

    def get_annotations_path(self) -> str:
        return f"{self._PATH.parent.joinpath('keras')}"

    def get_image_path(self) -> str:
        return f"{self._PATH.parent.joinpath('resources')}"

    def get_dirs_path(self) -> str:
        return f"{self._PATH.joinpath('ai')}"
