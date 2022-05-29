from typing import List


class Box:
    def __init__(self, x_min: int, x_max: int, y_min: int, y_max: int):
        self.__x_min = x_min
        self.__x_max = x_max
        self.__y_min = y_min
        self.__y_max = y_max

    def get_coors(self) -> List[int]:
        return [self.__x_min, self.__y_min, self.__x_max, self.__y_max]
