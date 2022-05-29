from src.model.box import Box


class Tag:
    def __init__(self, box: Box, tag_name: str):
        self.__box = box
        self.__tag_name = tag_name

    def get_box(self) -> Box:
        return self.__box

    def get_tag_name(self) -> str:
        return self.__tag_name
