import unittest

import cv2

from src.image.box_dto import BoxDTO
from src.image.extracting_service import ExtractingService


class ExtractingServiceTest(unittest.TestCase):
    service = ExtractingService()
    image: any
    cropped_image: any
    box: BoxDTO

    def test(self):
        # given
        self.image = cv2.imread("../resources/test.jpg")
        self.box = BoxDTO(290, 400, 309, 419)

        # when
        self.extract()

        # then
        self.assert_cropped_size()
        cv2.imshow("cropped", self.cropped_image)

    def extract(self):
        self.cropped_image = self.service.extract(self.box, self.image)

    def assert_cropped_size(self):
        self.assertEquals(self.box.get_shape()[0], self.cropped_image.shape[0])
        self.assertEquals(self.box.get_shape()[1], self.cropped_image.shape[1])
