from typing import List

from src.box import Box


class Annotation:
    def __init__(self, width: int, height: int):
        self.__boxes: List[Box] = []
        self.__width = width
        self.__height = height

    def push(self, box: Box):
        self.__boxes.append(box)

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def get_boxes(self) -> List[Box]:
        return self.__boxes
