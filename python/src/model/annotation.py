from typing import List

from src.model.tag import Tag


class Annotation:
    def __init__(self, width: int, height: int):
        self.__tags: List[Tag] = []
        self.__width = width
        self.__height = height

    def push(self, tag: Tag):
        self.__tags.append(tag)

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def get_tags(self) -> List[Tag]:
        return self.__tags
